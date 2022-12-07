from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ChatViewpoint(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new chatViewpoint and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether the chat is hidden for the current user.
        self._is_hidden: Optional[bool] = None
        # Represents the dateTime up until which the current user has read chatMessages in a specific chat.
        self._last_message_read_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatViewpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatViewpoint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatViewpoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_hidden": lambda n : setattr(self, 'is_hidden', n.get_bool_value()),
            "last_message_read_date_time": lambda n : setattr(self, 'last_message_read_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_hidden(self,) -> Optional[bool]:
        """
        Gets the isHidden property value. Indicates whether the chat is hidden for the current user.
        Returns: Optional[bool]
        """
        return self._is_hidden
    
    @is_hidden.setter
    def is_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHidden property value. Indicates whether the chat is hidden for the current user.
        Args:
            value: Value to set for the isHidden property.
        """
        self._is_hidden = value
    
    @property
    def last_message_read_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastMessageReadDateTime property value. Represents the dateTime up until which the current user has read chatMessages in a specific chat.
        Returns: Optional[datetime]
        """
        return self._last_message_read_date_time
    
    @last_message_read_date_time.setter
    def last_message_read_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastMessageReadDateTime property value. Represents the dateTime up until which the current user has read chatMessages in a specific chat.
        Args:
            value: Value to set for the lastMessageReadDateTime property.
        """
        self._last_message_read_date_time = value
    
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
        writer.write_bool_value("isHidden", self.is_hidden)
        writer.write_datetime_value("lastMessageReadDateTime", self.last_message_read_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

