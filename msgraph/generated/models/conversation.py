from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conversation_thread import ConversationThread
    from .entity import Entity

from .entity import Entity

@dataclass
class Conversation(Entity, Parsable):
    # Indicates whether any of the posts within this Conversation has at least one attachment. Supports $filter (eq, ne) and $search.
    has_attachments: Optional[bool] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_delivered_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A short summary from the body of the latest post in this conversation. Supports $filter (eq, ne, le, ge).
    preview: Optional[str] = None
    # A collection of all the conversation threads in the conversation. A navigation property. Read-only. Nullable.
    threads: Optional[list[ConversationThread]] = None
    # The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.
    topic: Optional[str] = None
    # All the users that sent a message to this Conversation.
    unique_senders: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Conversation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Conversation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Conversation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conversation_thread import ConversationThread
        from .entity import Entity

        from .conversation_thread import ConversationThread
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "hasAttachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "lastDeliveredDateTime": lambda n : setattr(self, 'last_delivered_date_time', n.get_datetime_value()),
            "preview": lambda n : setattr(self, 'preview', n.get_str_value()),
            "threads": lambda n : setattr(self, 'threads', n.get_collection_of_object_values(ConversationThread)),
            "topic": lambda n : setattr(self, 'topic', n.get_str_value()),
            "uniqueSenders": lambda n : setattr(self, 'unique_senders', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_datetime_value("lastDeliveredDateTime", self.last_delivered_date_time)
        writer.write_str_value("preview", self.preview)
        writer.write_collection_of_object_values("threads", self.threads)
        writer.write_str_value("topic", self.topic)
        writer.write_collection_of_primitive_values("uniqueSenders", self.unique_senders)
    

