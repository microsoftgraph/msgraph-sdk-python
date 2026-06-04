from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WebauthnAuthenticatorSelectionCriteria(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Specifies the preferred attachment modality for the authenticator. Possible values: platform (device-bound authenticator, such as Windows Hello), cross-platform (removable authenticator, such as a USB security key), or null (no preference).
    authenticator_attachment: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the authenticator must create a client-side-resident credential (also known as a discoverable credential). If true, the credential can be used without providing a credential ID.
    require_resident_key: Optional[bool] = None
    # Specifies the relying party's preference for user verification during credential creation. Possible values: required, preferred, or discouraged.
    user_verification: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebauthnAuthenticatorSelectionCriteria:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebauthnAuthenticatorSelectionCriteria
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebauthnAuthenticatorSelectionCriteria()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "authenticatorAttachment": lambda n : setattr(self, 'authenticator_attachment', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requireResidentKey": lambda n : setattr(self, 'require_resident_key', n.get_bool_value()),
            "userVerification": lambda n : setattr(self, 'user_verification', n.get_str_value()),
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
        writer.write_str_value("authenticatorAttachment", self.authenticator_attachment)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("requireResidentKey", self.require_resident_key)
        writer.write_str_value("userVerification", self.user_verification)
        writer.write_additional_data_value(self.additional_data)
    

