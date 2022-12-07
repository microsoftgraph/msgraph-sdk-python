from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

chat_message = lazy_import('msgraph.generated.models.chat_message')
entity = lazy_import('msgraph.generated.models.entity')

class PinnedChatMessageInfo(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new pinnedChatMessageInfo and sets the default values.
        """
        super().__init__()
        # Represents details about the chat message that is pinned.
        self._message: Optional[chat_message.ChatMessage] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PinnedChatMessageInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PinnedChatMessageInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PinnedChatMessageInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "message": lambda n : setattr(self, 'message', n.get_object_value(chat_message.ChatMessage)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def message(self,) -> Optional[chat_message.ChatMessage]:
        """
        Gets the message property value. Represents details about the chat message that is pinned.
        Returns: Optional[chat_message.ChatMessage]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[chat_message.ChatMessage] = None) -> None:
        """
        Sets the message property value. Represents details about the chat message that is pinned.
        Args:
            value: Value to set for the message property.
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
        super().serialize(writer)
        writer.write_object_value("message", self.message)
    

