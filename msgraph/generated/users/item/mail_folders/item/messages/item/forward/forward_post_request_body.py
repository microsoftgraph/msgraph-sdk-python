from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

message = lazy_import('msgraph.generated.models.message')
recipient = lazy_import('msgraph.generated.models.recipient')

class ForwardPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the forward method.
    """
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
    def comment(self,) -> Optional[str]:
        """
        Gets the comment property value. The Comment property
        Returns: Optional[str]
        """
        return self._comment
    
    @comment.setter
    def comment(self,value: Optional[str] = None) -> None:
        """
        Sets the comment property value. The Comment property
        Args:
            value: Value to set for the Comment property.
        """
        self._comment = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new forwardPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Comment property
        self._comment: Optional[str] = None
        # The Message property
        self._message: Optional[message.Message] = None
        # The ToRecipients property
        self._to_recipients: Optional[List[recipient.Recipient]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ForwardPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ForwardPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ForwardPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_object_value(message.Message)),
            "to_recipients": lambda n : setattr(self, 'to_recipients', n.get_collection_of_object_values(recipient.Recipient)),
        }
        return fields
    
    @property
    def message(self,) -> Optional[message.Message]:
        """
        Gets the message property value. The Message property
        Returns: Optional[message.Message]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[message.Message] = None) -> None:
        """
        Sets the message property value. The Message property
        Args:
            value: Value to set for the Message property.
        """
        self._message = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("Comment", self.comment)
        writer.write_object_value("Message", self.message)
        writer.write_collection_of_object_values("ToRecipients", self.to_recipients)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def to_recipients(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the toRecipients property value. The ToRecipients property
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._to_recipients
    
    @to_recipients.setter
    def to_recipients(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the toRecipients property value. The ToRecipients property
        Args:
            value: Value to set for the ToRecipients property.
        """
        self._to_recipients = value
    

