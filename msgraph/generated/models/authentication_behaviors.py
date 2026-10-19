from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AuthenticationBehaviors(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # If false, allows the app to have extended access to Azure AD Graph until August 31, 2025 when Azure AD Graph is fully retired. For more information on Azure AD retirement updates, see June 2024 update on Azure AD Graph API retirement.
    block_azure_a_d_graph_access: Optional[bool] = None
    # Indicates whether Cross-Origin-Opener-Policy (COOP) headers are enforced on browser-based authentication responses for the application. Set to true to enable enforcement, false to temporarily suppress enforcement, or null to use the service default. For how-to guidance, see Control Cross-Origin-Opener-Policy enforcement.
    coop_enforcement: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If true, removes the email claim from tokens sent to an application when the email address's domain can't be verified.
    remove_unverified_email_claim: Optional[bool] = None
    # If true, requires multitenant applications to have a service principal in the resource tenant as part of authorization checks before they're granted access tokens. This property is only modifiable for multitenant resource applications that rely on access from clients without a service principal and had this behavior as set to false by Microsoft. Tenant administrators should respond to security advisories sent through Azure Health Service events and the Microsoft 365 message center.
    require_client_service_principal: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationBehaviors:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationBehaviors
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationBehaviors()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "blockAzureADGraphAccess": lambda n : setattr(self, 'block_azure_a_d_graph_access', n.get_bool_value()),
            "coopEnforcement": lambda n : setattr(self, 'coop_enforcement', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "removeUnverifiedEmailClaim": lambda n : setattr(self, 'remove_unverified_email_claim', n.get_bool_value()),
            "requireClientServicePrincipal": lambda n : setattr(self, 'require_client_service_principal', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("blockAzureADGraphAccess", self.block_azure_a_d_graph_access)
        writer.write_bool_value("coopEnforcement", self.coop_enforcement)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("removeUnverifiedEmailClaim", self.remove_unverified_email_claim)
        writer.write_bool_value("requireClientServicePrincipal", self.require_client_service_principal)
        writer.write_additional_data_value(self.additional_data)
    

