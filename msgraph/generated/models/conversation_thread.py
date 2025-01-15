from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .post import Post
    from .recipient import Recipient

from .entity import Entity

@dataclass
class ConversationThread(Entity, Parsable):
    # The Cc: recipients for the thread. Returned only on $select.
    cc_recipients: Optional[list[Recipient]] = None
    # Indicates whether any of the posts within this thread has at least one attachment. Returned by default.
    has_attachments: Optional[bool] = None
    # Indicates if the thread is locked. Returned by default.
    is_locked: Optional[bool] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.Returned by default.
    last_delivered_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The posts property
    posts: Optional[list[Post]] = None
    # A short summary from the body of the latest post in this conversation. Returned by default.
    preview: Optional[str] = None
    # The To: recipients for the thread. Returned only on $select.
    to_recipients: Optional[list[Recipient]] = None
    # The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated. Returned by default.
    topic: Optional[str] = None
    # All the users that sent a message to this thread. Returned by default.
    unique_senders: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConversationThread:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConversationThread
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConversationThread()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .post import Post
        from .recipient import Recipient

        from .entity import Entity
        from .post import Post
        from .recipient import Recipient

        fields: dict[str, Callable[[Any], None]] = {
            "ccRecipients": lambda n : setattr(self, 'cc_recipients', n.get_collection_of_object_values(Recipient)),
            "hasAttachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "isLocked": lambda n : setattr(self, 'is_locked', n.get_bool_value()),
            "lastDeliveredDateTime": lambda n : setattr(self, 'last_delivered_date_time', n.get_datetime_value()),
            "posts": lambda n : setattr(self, 'posts', n.get_collection_of_object_values(Post)),
            "preview": lambda n : setattr(self, 'preview', n.get_str_value()),
            "toRecipients": lambda n : setattr(self, 'to_recipients', n.get_collection_of_object_values(Recipient)),
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
        writer.write_collection_of_object_values("ccRecipients", self.cc_recipients)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_bool_value("isLocked", self.is_locked)
        writer.write_datetime_value("lastDeliveredDateTime", self.last_delivered_date_time)
        writer.write_collection_of_object_values("posts", self.posts)
        writer.write_str_value("preview", self.preview)
        writer.write_collection_of_object_values("toRecipients", self.to_recipients)
        writer.write_str_value("topic", self.topic)
        writer.write_collection_of_primitive_values("uniqueSenders", self.unique_senders)
    

