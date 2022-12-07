from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

recipient = lazy_import('msgraph.generated.models.recipient')

class InvitedUserMessageInfo(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def cc_recipients(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the ccRecipients property value. Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._cc_recipients
    
    @cc_recipients.setter
    def cc_recipients(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the ccRecipients property value. Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.
        Args:
            value: Value to set for the ccRecipients property.
        """
        self._cc_recipients = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new invitedUserMessageInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.
        self._cc_recipients: Optional[List[recipient.Recipient]] = None
        # Customized message body you want to send if you don't want the default message.
        self._customized_message_body: Optional[str] = None
        # The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.
        self._message_language: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InvitedUserMessageInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InvitedUserMessageInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InvitedUserMessageInfo()
    
    @property
    def customized_message_body(self,) -> Optional[str]:
        """
        Gets the customizedMessageBody property value. Customized message body you want to send if you don't want the default message.
        Returns: Optional[str]
        """
        return self._customized_message_body
    
    @customized_message_body.setter
    def customized_message_body(self,value: Optional[str] = None) -> None:
        """
        Sets the customizedMessageBody property value. Customized message body you want to send if you don't want the default message.
        Args:
            value: Value to set for the customizedMessageBody property.
        """
        self._customized_message_body = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cc_recipients": lambda n : setattr(self, 'cc_recipients', n.get_collection_of_object_values(recipient.Recipient)),
            "customized_message_body": lambda n : setattr(self, 'customized_message_body', n.get_str_value()),
            "message_language": lambda n : setattr(self, 'message_language', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def message_language(self,) -> Optional[str]:
        """
        Gets the messageLanguage property value. The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.
        Returns: Optional[str]
        """
        return self._message_language
    
    @message_language.setter
    def message_language(self,value: Optional[str] = None) -> None:
        """
        Sets the messageLanguage property value. The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.
        Args:
            value: Value to set for the messageLanguage property.
        """
        self._message_language = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("ccRecipients", self.cc_recipients)
        writer.write_str_value("customizedMessageBody", self.customized_message_body)
        writer.write_str_value("messageLanguage", self.message_language)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

