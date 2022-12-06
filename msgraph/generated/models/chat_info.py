from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ChatInfo(AdditionalDataHolder, Parsable):
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
        Instantiates a new chatInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The unique identifier of a message in a Microsoft Teams channel.
        self._message_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The ID of the reply message.
        self._reply_chain_message_id: Optional[str] = None
        # The unique identifier for a thread in Microsoft Teams.
        self._thread_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "message_id": lambda n : setattr(self, 'message_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reply_chain_message_id": lambda n : setattr(self, 'reply_chain_message_id', n.get_str_value()),
            "thread_id": lambda n : setattr(self, 'thread_id', n.get_str_value()),
        }
        return fields
    
    @property
    def message_id(self,) -> Optional[str]:
        """
        Gets the messageId property value. The unique identifier of a message in a Microsoft Teams channel.
        Returns: Optional[str]
        """
        return self._message_id
    
    @message_id.setter
    def message_id(self,value: Optional[str] = None) -> None:
        """
        Sets the messageId property value. The unique identifier of a message in a Microsoft Teams channel.
        Args:
            value: Value to set for the messageId property.
        """
        self._message_id = value
    
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
    
    @property
    def reply_chain_message_id(self,) -> Optional[str]:
        """
        Gets the replyChainMessageId property value. The ID of the reply message.
        Returns: Optional[str]
        """
        return self._reply_chain_message_id
    
    @reply_chain_message_id.setter
    def reply_chain_message_id(self,value: Optional[str] = None) -> None:
        """
        Sets the replyChainMessageId property value. The ID of the reply message.
        Args:
            value: Value to set for the replyChainMessageId property.
        """
        self._reply_chain_message_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("messageId", self.message_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("replyChainMessageId", self.reply_chain_message_id)
        writer.write_str_value("threadId", self.thread_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def thread_id(self,) -> Optional[str]:
        """
        Gets the threadId property value. The unique identifier for a thread in Microsoft Teams.
        Returns: Optional[str]
        """
        return self._thread_id
    
    @thread_id.setter
    def thread_id(self,value: Optional[str] = None) -> None:
        """
        Sets the threadId property value. The unique identifier for a thread in Microsoft Teams.
        Args:
            value: Value to set for the threadId property.
        """
        self._thread_id = value
    

