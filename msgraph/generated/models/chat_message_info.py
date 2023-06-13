from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import chat_message_from_identity_set, chat_message_type, entity, event_message_detail, item_body

from . import entity

@dataclass
class ChatMessageInfo(entity.Entity):
    # Body of the chatMessage. This will still contain markers for @mentions and attachments even though the object does not return @mentions and attachments.
    body: Optional[item_body.ItemBody] = None
    # Date time object representing the time at which message was created.
    created_date_time: Optional[datetime] = None
    # Read-only.  If present, represents details of an event that happened in a chat, a channel, or a team, for example, members were added, and so on. For event messages, the messageType property will be set to systemEventMessage.
    event_detail: Optional[event_message_detail.EventMessageDetail] = None
    # Information about the sender of the message.
    from_: Optional[chat_message_from_identity_set.ChatMessageFromIdentitySet] = None
    # If set to true, the original message has been deleted.
    is_deleted: Optional[bool] = None
    # The messageType property
    message_type: Optional[chat_message_type.ChatMessageType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessageInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMessageInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import chat_message_from_identity_set, chat_message_type, entity, event_message_detail, item_body

        fields: Dict[str, Callable[[Any], None]] = {
            "body": lambda n : setattr(self, 'body', n.get_object_value(item_body.ItemBody)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "eventDetail": lambda n : setattr(self, 'event_detail', n.get_object_value(event_message_detail.EventMessageDetail)),
            "from": lambda n : setattr(self, 'from_', n.get_object_value(chat_message_from_identity_set.ChatMessageFromIdentitySet)),
            "isDeleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "messageType": lambda n : setattr(self, 'message_type', n.get_enum_value(chat_message_type.ChatMessageType)),
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
        writer.write_object_value("body", self.body)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("eventDetail", self.event_detail)
        writer.write_object_value("from", self.from_)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_enum_value("messageType", self.message_type)
    

