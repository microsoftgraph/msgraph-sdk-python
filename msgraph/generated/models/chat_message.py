from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .channel_identity import ChannelIdentity
    from .chat_message_attachment import ChatMessageAttachment
    from .chat_message_from_identity_set import ChatMessageFromIdentitySet
    from .chat_message_history_item import ChatMessageHistoryItem
    from .chat_message_hosted_content import ChatMessageHostedContent
    from .chat_message_importance import ChatMessageImportance
    from .chat_message_mention import ChatMessageMention
    from .chat_message_policy_violation import ChatMessagePolicyViolation
    from .chat_message_reaction import ChatMessageReaction
    from .chat_message_type import ChatMessageType
    from .entity import Entity
    from .event_message_detail import EventMessageDetail
    from .item_body import ItemBody

from .entity import Entity

@dataclass
class ChatMessage(Entity, Parsable):
    # References to attached objects like files, tabs, meetings etc.
    attachments: Optional[list[ChatMessageAttachment]] = None
    # The body property
    body: Optional[ItemBody] = None
    # If the message was sent in a channel, represents identity of the channel.
    channel_identity: Optional[ChannelIdentity] = None
    # If the message was sent in a chat, represents the identity of the chat.
    chat_id: Optional[str] = None
    # Timestamp of when the chat message was created.
    created_date_time: Optional[datetime.datetime] = None
    # Read only. Timestamp at which the chat message was deleted, or null if not deleted.
    deleted_date_time: Optional[datetime.datetime] = None
    # Read-only. Version number of the chat message.
    etag: Optional[str] = None
    # Read-only. If present, represents details of an event that happened in a chat, a channel, or a team, for example, adding new members. For event messages, the messageType property will be set to systemEventMessage.
    event_detail: Optional[EventMessageDetail] = None
    # Details of the sender of the chat message. Can only be set during migration.
    from_: Optional[ChatMessageFromIdentitySet] = None
    # Content in a message hosted by Microsoft Teams - for example, images or code snippets.
    hosted_contents: Optional[list[ChatMessageHostedContent]] = None
    # The importance property
    importance: Optional[ChatMessageImportance] = None
    # Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Teams UI. If no edits are made the value is null.
    last_edited_date_time: Optional[datetime.datetime] = None
    # Read only. Timestamp when the chat message is created (initial setting) or modified, including when a reaction is added or removed.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Locale of the chat message set by the client. Always set to en-us.
    locale: Optional[str] = None
    # List of entities mentioned in the chat message. Supported entities are: user, bot, team, channel, chat, and tag.
    mentions: Optional[list[ChatMessageMention]] = None
    # List of activity history of a message item, including modification time and actions, such as reactionAdded, reactionRemoved, or reaction changes, on the message.
    message_history: Optional[list[ChatMessageHistoryItem]] = None
    # The messageType property
    message_type: Optional[ChatMessageType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines the properties of a policy violation set by a data loss prevention (DLP) application.
    policy_violation: Optional[ChatMessagePolicyViolation] = None
    # Reactions for this chat message (for example, Like).
    reactions: Optional[list[ChatMessageReaction]] = None
    # Replies for a specified message. Supports $expand for channel messages.
    replies: Optional[list[ChatMessage]] = None
    # Read-only. ID of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels, not chats.)
    reply_to_id: Optional[str] = None
    # The subject of the chat message, in plaintext.
    subject: Optional[str] = None
    # Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.
    summary: Optional[str] = None
    # Read-only. Link to the message in Microsoft Teams.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChatMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChatMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .channel_identity import ChannelIdentity
        from .chat_message_attachment import ChatMessageAttachment
        from .chat_message_from_identity_set import ChatMessageFromIdentitySet
        from .chat_message_history_item import ChatMessageHistoryItem
        from .chat_message_hosted_content import ChatMessageHostedContent
        from .chat_message_importance import ChatMessageImportance
        from .chat_message_mention import ChatMessageMention
        from .chat_message_policy_violation import ChatMessagePolicyViolation
        from .chat_message_reaction import ChatMessageReaction
        from .chat_message_type import ChatMessageType
        from .entity import Entity
        from .event_message_detail import EventMessageDetail
        from .item_body import ItemBody

        from .channel_identity import ChannelIdentity
        from .chat_message_attachment import ChatMessageAttachment
        from .chat_message_from_identity_set import ChatMessageFromIdentitySet
        from .chat_message_history_item import ChatMessageHistoryItem
        from .chat_message_hosted_content import ChatMessageHostedContent
        from .chat_message_importance import ChatMessageImportance
        from .chat_message_mention import ChatMessageMention
        from .chat_message_policy_violation import ChatMessagePolicyViolation
        from .chat_message_reaction import ChatMessageReaction
        from .chat_message_type import ChatMessageType
        from .entity import Entity
        from .event_message_detail import EventMessageDetail
        from .item_body import ItemBody

        fields: dict[str, Callable[[Any], None]] = {
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(ChatMessageAttachment)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "channelIdentity": lambda n : setattr(self, 'channel_identity', n.get_object_value(ChannelIdentity)),
            "chatId": lambda n : setattr(self, 'chat_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "etag": lambda n : setattr(self, 'etag', n.get_str_value()),
            "eventDetail": lambda n : setattr(self, 'event_detail', n.get_object_value(EventMessageDetail)),
            "from": lambda n : setattr(self, 'from_', n.get_object_value(ChatMessageFromIdentitySet)),
            "hostedContents": lambda n : setattr(self, 'hosted_contents', n.get_collection_of_object_values(ChatMessageHostedContent)),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(ChatMessageImportance)),
            "lastEditedDateTime": lambda n : setattr(self, 'last_edited_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "mentions": lambda n : setattr(self, 'mentions', n.get_collection_of_object_values(ChatMessageMention)),
            "messageHistory": lambda n : setattr(self, 'message_history', n.get_collection_of_object_values(ChatMessageHistoryItem)),
            "messageType": lambda n : setattr(self, 'message_type', n.get_enum_value(ChatMessageType)),
            "policyViolation": lambda n : setattr(self, 'policy_violation', n.get_object_value(ChatMessagePolicyViolation)),
            "reactions": lambda n : setattr(self, 'reactions', n.get_collection_of_object_values(ChatMessageReaction)),
            "replies": lambda n : setattr(self, 'replies', n.get_collection_of_object_values(ChatMessage)),
            "replyToId": lambda n : setattr(self, 'reply_to_id', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_object_value("body", self.body)
        writer.write_object_value("channelIdentity", self.channel_identity)
        writer.write_str_value("chatId", self.chat_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
        writer.write_str_value("etag", self.etag)
        writer.write_object_value("eventDetail", self.event_detail)
        writer.write_object_value("from", self.from_)
        writer.write_collection_of_object_values("hostedContents", self.hosted_contents)
        writer.write_enum_value("importance", self.importance)
        writer.write_datetime_value("lastEditedDateTime", self.last_edited_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("locale", self.locale)
        writer.write_collection_of_object_values("mentions", self.mentions)
        writer.write_collection_of_object_values("messageHistory", self.message_history)
        writer.write_enum_value("messageType", self.message_type)
        writer.write_object_value("policyViolation", self.policy_violation)
        writer.write_collection_of_object_values("reactions", self.reactions)
        writer.write_collection_of_object_values("replies", self.replies)
        writer.write_str_value("replyToId", self.reply_to_id)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("summary", self.summary)
        writer.write_str_value("webUrl", self.web_url)
    

