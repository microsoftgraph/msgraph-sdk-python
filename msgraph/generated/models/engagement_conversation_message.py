from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .engagement_conversation import EngagementConversation
    from .engagement_conversation_discussion_message import EngagementConversationDiscussionMessage
    from .engagement_conversation_message_reaction import EngagementConversationMessageReaction
    from .engagement_conversation_question_message import EngagementConversationQuestionMessage
    from .engagement_conversation_system_message import EngagementConversationSystemMessage
    from .engagement_creation_mode import EngagementCreationMode
    from .engagement_identity_set import EngagementIdentitySet
    from .entity import Entity
    from .item_body import ItemBody

from .entity import Entity

@dataclass
class EngagementConversationMessage(Entity, Parsable):
    """
    A Viva Engage conversation message.
    """
    # The body property
    body: Optional[ItemBody] = None
    # The conversation property
    conversation: Optional[EngagementConversation] = None
    # The date and time when the message was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Indicates that the resource is in migration state and is currently being used for migration purposes.
    creation_mode: Optional[EngagementCreationMode] = None
    # Identity of the sender of the message.
    from_: Optional[EngagementIdentitySet] = None
    # The date and time when message was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of reactions (such as like and smile) that users have applied to this message.
    reactions: Optional[list[EngagementConversationMessageReaction]] = None
    # A collection of messages that are replies to this message and form a threaded discussion.
    replies: Optional[list[EngagementConversationMessage]] = None
    # The parent message to which this message is a reply, if it is part of a reply chain.
    reply_to: Optional[EngagementConversationMessage] = None
    # The ID of the parent message to which this message is a reply, if applicable.
    reply_to_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EngagementConversationMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EngagementConversationMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementConversationDiscussionMessage".casefold():
            from .engagement_conversation_discussion_message import EngagementConversationDiscussionMessage

            return EngagementConversationDiscussionMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementConversationQuestionMessage".casefold():
            from .engagement_conversation_question_message import EngagementConversationQuestionMessage

            return EngagementConversationQuestionMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementConversationSystemMessage".casefold():
            from .engagement_conversation_system_message import EngagementConversationSystemMessage

            return EngagementConversationSystemMessage()
        return EngagementConversationMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .engagement_conversation import EngagementConversation
        from .engagement_conversation_discussion_message import EngagementConversationDiscussionMessage
        from .engagement_conversation_message_reaction import EngagementConversationMessageReaction
        from .engagement_conversation_question_message import EngagementConversationQuestionMessage
        from .engagement_conversation_system_message import EngagementConversationSystemMessage
        from .engagement_creation_mode import EngagementCreationMode
        from .engagement_identity_set import EngagementIdentitySet
        from .entity import Entity
        from .item_body import ItemBody

        from .engagement_conversation import EngagementConversation
        from .engagement_conversation_discussion_message import EngagementConversationDiscussionMessage
        from .engagement_conversation_message_reaction import EngagementConversationMessageReaction
        from .engagement_conversation_question_message import EngagementConversationQuestionMessage
        from .engagement_conversation_system_message import EngagementConversationSystemMessage
        from .engagement_creation_mode import EngagementCreationMode
        from .engagement_identity_set import EngagementIdentitySet
        from .entity import Entity
        from .item_body import ItemBody

        fields: dict[str, Callable[[Any], None]] = {
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "conversation": lambda n : setattr(self, 'conversation', n.get_object_value(EngagementConversation)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creationMode": lambda n : setattr(self, 'creation_mode', n.get_enum_value(EngagementCreationMode)),
            "from": lambda n : setattr(self, 'from_', n.get_object_value(EngagementIdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "reactions": lambda n : setattr(self, 'reactions', n.get_collection_of_object_values(EngagementConversationMessageReaction)),
            "replies": lambda n : setattr(self, 'replies', n.get_collection_of_object_values(EngagementConversationMessage)),
            "replyTo": lambda n : setattr(self, 'reply_to', n.get_object_value(EngagementConversationMessage)),
            "replyToId": lambda n : setattr(self, 'reply_to_id', n.get_str_value()),
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
        writer.write_object_value("conversation", self.conversation)
        writer.write_enum_value("creationMode", self.creation_mode)
        writer.write_object_value("from", self.from_)
        writer.write_collection_of_object_values("reactions", self.reactions)
        writer.write_collection_of_object_values("replies", self.replies)
        writer.write_object_value("replyTo", self.reply_to)
        writer.write_str_value("replyToId", self.reply_to_id)
    

