from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fraud_protection_provider import FraudProtectionProvider
    from .web_application_firewall_provider import WebApplicationFirewallProvider
    from .web_application_firewall_verification_model import WebApplicationFirewallVerificationModel

@dataclass
class RiskPreventionContainer(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Represents entry point for fraud protection provider configurations for Microsoft Entra External ID tenants.
    fraud_protection_providers: Optional[list[FraudProtectionProvider]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of WAF provider configurations registered in the External ID tenant.
    web_application_firewall_providers: Optional[list[WebApplicationFirewallProvider]] = None
    # Collection of verification operations performed for domains or hosts with WAF providers registered in the External ID tenant.
    web_application_firewall_verifications: Optional[list[WebApplicationFirewallVerificationModel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RiskPreventionContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RiskPreventionContainer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RiskPreventionContainer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .fraud_protection_provider import FraudProtectionProvider
        from .web_application_firewall_provider import WebApplicationFirewallProvider
        from .web_application_firewall_verification_model import WebApplicationFirewallVerificationModel

        from .fraud_protection_provider import FraudProtectionProvider
        from .web_application_firewall_provider import WebApplicationFirewallProvider
        from .web_application_firewall_verification_model import WebApplicationFirewallVerificationModel

        fields: dict[str, Callable[[Any], None]] = {
            "fraudProtectionProviders": lambda n : setattr(self, 'fraud_protection_providers', n.get_collection_of_object_values(FraudProtectionProvider)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "webApplicationFirewallProviders": lambda n : setattr(self, 'web_application_firewall_providers', n.get_collection_of_object_values(WebApplicationFirewallProvider)),
            "webApplicationFirewallVerifications": lambda n : setattr(self, 'web_application_firewall_verifications', n.get_collection_of_object_values(WebApplicationFirewallVerificationModel)),
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
        writer.write_collection_of_object_values("fraudProtectionProviders", self.fraud_protection_providers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("webApplicationFirewallProviders", self.web_application_firewall_providers)
        writer.write_collection_of_object_values("webApplicationFirewallVerifications", self.web_application_firewall_verifications)
        writer.write_additional_data_value(self.additional_data)
    

