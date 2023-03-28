from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teamwork_notification_recipient

from . import teamwork_notification_recipient

class ChatMembersNotificationRecipient(teamwork_notification_recipient.TeamworkNotificationRecipient):
    def __init__(self,) -> None:
        """
        Instantiates a new ChatMembersNotificationRecipient and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.chatMembersNotificationRecipient"
        # The unique identifier for the chat whose members should receive the notifications.
        self._chat_id: Optional[str] = None
    
    @property
    def chat_id(self,) -> Optional[str]:
        """
        Gets the chatId property value. The unique identifier for the chat whose members should receive the notifications.
        Returns: Optional[str]
        """
        return self._chat_id
    
    @chat_id.setter
    def chat_id(self,value: Optional[str] = None) -> None:
        """
        Sets the chatId property value. The unique identifier for the chat whose members should receive the notifications.
        Args:
            value: Value to set for the chat_id property.
        """
        self._chat_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMembersNotificationRecipient:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMembersNotificationRecipient
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMembersNotificationRecipient()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teamwork_notification_recipient

        fields: Dict[str, Callable[[Any], None]] = {
            "chatId": lambda n : setattr(self, 'chat_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("chatId", self.chat_id)
    

