from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_message_from_identity_set import ChatMessageFromIdentitySet
    from .chat_message_type import ChatMessageType
    from .entity import Entity
    from .event_message_detail import EventMessageDetail
    from .item_body import ItemBody

from .entity import Entity

@dataclass
class ChatMessageInfo(Entity, Parsable):
    # Body of the chatMessage. This will still contain markers for @mentions and attachments even though the object doesn't return @mentions and attachments.
    body: Optional[ItemBody] = None
    # Date time object representing the time at which message was created.
    created_date_time: Optional[datetime.datetime] = None
    # Read-only.  If present, represents details of an event that happened in a chat, a channel, or a team, for example, members were added, and so on. For event messages, the messageType property is set to systemEventMessage.
    event_detail: Optional[EventMessageDetail] = None
    # Information about the sender of the message.
    from_: Optional[ChatMessageFromIdentitySet] = None
    # If set to true, the original message has been deleted.
    is_deleted: Optional[bool] = None
    # The messageType property
    message_type: Optional[ChatMessageType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChatMessageInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChatMessageInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chat_message_from_identity_set import ChatMessageFromIdentitySet
        from .chat_message_type import ChatMessageType
        from .entity import Entity
        from .event_message_detail import EventMessageDetail
        from .item_body import ItemBody

        from .chat_message_from_identity_set import ChatMessageFromIdentitySet
        from .chat_message_type import ChatMessageType
        from .entity import Entity
        from .event_message_detail import EventMessageDetail
        from .item_body import ItemBody

        fields: dict[str, Callable[[Any], None]] = {
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "eventDetail": lambda n : setattr(self, 'event_detail', n.get_object_value(EventMessageDetail)),
            "from": lambda n : setattr(self, 'from_', n.get_object_value(ChatMessageFromIdentitySet)),
            "isDeleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "messageType": lambda n : setattr(self, 'message_type', n.get_enum_value(ChatMessageType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("body", self.body)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("eventDetail", self.event_detail)
        writer.write_object_value("from", self.from_)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_enum_value("messageType", self.message_type)
    

