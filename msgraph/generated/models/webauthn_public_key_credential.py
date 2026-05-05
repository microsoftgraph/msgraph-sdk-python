from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .webauthn_authentication_extensions_client_outputs import WebauthnAuthenticationExtensionsClientOutputs
    from .webauthn_authenticator_attestation_response import WebauthnAuthenticatorAttestationResponse

@dataclass
class WebauthnPublicKeyCredential(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The clientExtensionResults property
    client_extension_results: Optional[WebauthnAuthenticationExtensionsClientOutputs] = None
    # The id property
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The response property
    response: Optional[WebauthnAuthenticatorAttestationResponse] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebauthnPublicKeyCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebauthnPublicKeyCredential
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebauthnPublicKeyCredential()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .webauthn_authentication_extensions_client_outputs import WebauthnAuthenticationExtensionsClientOutputs
        from .webauthn_authenticator_attestation_response import WebauthnAuthenticatorAttestationResponse

        from .webauthn_authentication_extensions_client_outputs import WebauthnAuthenticationExtensionsClientOutputs
        from .webauthn_authenticator_attestation_response import WebauthnAuthenticatorAttestationResponse

        fields: dict[str, Callable[[Any], None]] = {
            "clientExtensionResults": lambda n : setattr(self, 'client_extension_results', n.get_object_value(WebauthnAuthenticationExtensionsClientOutputs)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "response": lambda n : setattr(self, 'response', n.get_object_value(WebauthnAuthenticatorAttestationResponse)),
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
        writer.write_object_value("clientExtensionResults", self.client_extension_results)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("response", self.response)
        writer.write_additional_data_value(self.additional_data)
    

