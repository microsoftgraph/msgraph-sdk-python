from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AcceptPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the accept method.
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
        Instantiates a new acceptPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Comment property
        self._comment: Optional[str] = None
        # The SendResponse property
        self._send_response: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AcceptPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AcceptPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AcceptPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "send_response": lambda n : setattr(self, 'send_response', n.get_bool_value()),
        }
        return fields
    
    @property
    def send_response(self,) -> Optional[bool]:
        """
        Gets the sendResponse property value. The SendResponse property
        Returns: Optional[bool]
        """
        return self._send_response
    
    @send_response.setter
    def send_response(self,value: Optional[bool] = None) -> None:
        """
        Sets the sendResponse property value. The SendResponse property
        Args:
            value: Value to set for the SendResponse property.
        """
        self._send_response = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("Comment", self.comment)
        writer.write_bool_value("SendResponse", self.send_response)
        writer.write_additional_data_value(self.additional_data)
    

