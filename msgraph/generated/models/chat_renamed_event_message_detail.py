from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_message_detail, identity_set

from . import event_message_detail

@dataclass
class ChatRenamedEventMessageDetail(event_message_detail.EventMessageDetail):
    odata_type = "#microsoft.graph.chatRenamedEventMessageDetail"
    # The updated name of the chat.
    chat_display_name: Optional[str] = None
    # Unique identifier of the chat.
    chat_id: Optional[str] = None
    # Initiator of the event.
    initiator: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatRenamedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatRenamedEventMessageDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ChatRenamedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_message_detail, identity_set

        from . import event_message_detail, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "chatDisplayName": lambda n : setattr(self, 'chat_display_name', n.get_str_value()),
            "chatId": lambda n : setattr(self, 'chat_id', n.get_str_value()),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("chatDisplayName", self.chat_display_name)
        writer.write_str_value("chatId", self.chat_id)
        writer.write_object_value("initiator", self.initiator)
    

