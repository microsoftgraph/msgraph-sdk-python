from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .recipient import Recipient

@dataclass
class InvitedUserMessageInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Additional recipients the invitation message should be sent to. Currently only one additional recipient is supported.
    cc_recipients: Optional[List[Recipient]] = None
    # Customized message body you want to send if you don't want the default message.
    customized_message_body: Optional[str] = None
    # The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.
    message_language: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvitedUserMessageInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvitedUserMessageInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvitedUserMessageInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .recipient import Recipient

        from .recipient import Recipient

        fields: Dict[str, Callable[[Any], None]] = {
            "ccRecipients": lambda n : setattr(self, 'cc_recipients', n.get_collection_of_object_values(Recipient)),
            "customizedMessageBody": lambda n : setattr(self, 'customized_message_body', n.get_str_value()),
            "messageLanguage": lambda n : setattr(self, 'message_language', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("ccRecipients", self.cc_recipients)
        writer.write_str_value("customizedMessageBody", self.customized_message_body)
        writer.write_str_value("messageLanguage", self.message_language)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

