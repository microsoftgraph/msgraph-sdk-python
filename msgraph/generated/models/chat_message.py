from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import channel_identity, chat_message_attachment, chat_message_from_identity_set, chat_message_history_item, chat_message_hosted_content, chat_message_importance, chat_message_mention, chat_message_policy_violation, chat_message_reaction, chat_message_type, entity, event_message_detail, item_body

from . import entity

class ChatMessage(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new chatMessage and sets the default values.
        """
        super().__init__()
        # References to attached objects like files, tabs, meetings etc.
        self._attachments: Optional[List[chat_message_attachment.ChatMessageAttachment]] = None
        # The body property
        self._body: Optional[item_body.ItemBody] = None
        # If the message was sent in a channel, represents identity of the channel.
        self._channel_identity: Optional[channel_identity.ChannelIdentity] = None
        # If the message was sent in a chat, represents the identity of the chat.
        self._chat_id: Optional[str] = None
        # Timestamp of when the chat message was created.
        self._created_date_time: Optional[datetime] = None
        # Read only. Timestamp at which the chat message was deleted, or null if not deleted.
        self._deleted_date_time: Optional[datetime] = None
        # Read-only. Version number of the chat message.
        self._etag: Optional[str] = None
        # Read-only. If present, represents details of an event that happened in a chat, a channel, or a team, for example, adding new members. For event messages, the messageType property will be set to systemEventMessage.
        self._event_detail: Optional[event_message_detail.EventMessageDetail] = None
        # Details of the sender of the chat message. Can only be set during migration.
        self._from_: Optional[chat_message_from_identity_set.ChatMessageFromIdentitySet] = None
        # Content in a message hosted by Microsoft Teams - for example, images or code snippets.
        self._hosted_contents: Optional[List[chat_message_hosted_content.ChatMessageHostedContent]] = None
        # The importance property
        self._importance: Optional[chat_message_importance.ChatMessageImportance] = None
        # Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Teams UI. If no edits are made the value is null.
        self._last_edited_date_time: Optional[datetime] = None
        # Read only. Timestamp when the chat message is created (initial setting) or modified, including when a reaction is added or removed.
        self._last_modified_date_time: Optional[datetime] = None
        # Locale of the chat message set by the client. Always set to en-us.
        self._locale: Optional[str] = None
        # List of entities mentioned in the chat message. Supported entities are: user, bot, team, and channel.
        self._mentions: Optional[List[chat_message_mention.ChatMessageMention]] = None
        # The messageHistory property
        self._message_history: Optional[List[chat_message_history_item.ChatMessageHistoryItem]] = None
        # The messageType property
        self._message_type: Optional[chat_message_type.ChatMessageType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Defines the properties of a policy violation set by a data loss prevention (DLP) application.
        self._policy_violation: Optional[chat_message_policy_violation.ChatMessagePolicyViolation] = None
        # Reactions for this chat message (for example, Like).
        self._reactions: Optional[List[chat_message_reaction.ChatMessageReaction]] = None
        # Replies for a specified message. Supports $expand for channel messages.
        self._replies: Optional[List[ChatMessage]] = None
        # Read-only. ID of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels, not chats.)
        self._reply_to_id: Optional[str] = None
        # The subject of the chat message, in plaintext.
        self._subject: Optional[str] = None
        # Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.
        self._summary: Optional[str] = None
        # Read-only. Link to the message in Microsoft Teams.
        self._web_url: Optional[str] = None
    
    @property
    def attachments(self,) -> Optional[List[chat_message_attachment.ChatMessageAttachment]]:
        """
        Gets the attachments property value. References to attached objects like files, tabs, meetings etc.
        Returns: Optional[List[chat_message_attachment.ChatMessageAttachment]]
        """
        return self._attachments
    
    @attachments.setter
    def attachments(self,value: Optional[List[chat_message_attachment.ChatMessageAttachment]] = None) -> None:
        """
        Sets the attachments property value. References to attached objects like files, tabs, meetings etc.
        Args:
            value: Value to set for the attachments property.
        """
        self._attachments = value
    
    @property
    def body(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the body property value. The body property
        Returns: Optional[item_body.ItemBody]
        """
        return self._body
    
    @body.setter
    def body(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the body property value. The body property
        Args:
            value: Value to set for the body property.
        """
        self._body = value
    
    @property
    def channel_identity(self,) -> Optional[channel_identity.ChannelIdentity]:
        """
        Gets the channelIdentity property value. If the message was sent in a channel, represents identity of the channel.
        Returns: Optional[channel_identity.ChannelIdentity]
        """
        return self._channel_identity
    
    @channel_identity.setter
    def channel_identity(self,value: Optional[channel_identity.ChannelIdentity] = None) -> None:
        """
        Sets the channelIdentity property value. If the message was sent in a channel, represents identity of the channel.
        Args:
            value: Value to set for the channel_identity property.
        """
        self._channel_identity = value
    
    @property
    def chat_id(self,) -> Optional[str]:
        """
        Gets the chatId property value. If the message was sent in a chat, represents the identity of the chat.
        Returns: Optional[str]
        """
        return self._chat_id
    
    @chat_id.setter
    def chat_id(self,value: Optional[str] = None) -> None:
        """
        Sets the chatId property value. If the message was sent in a chat, represents the identity of the chat.
        Args:
            value: Value to set for the chat_id property.
        """
        self._chat_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Timestamp of when the chat message was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Timestamp of when the chat message was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMessage()
    
    @property
    def deleted_date_time(self,) -> Optional[datetime]:
        """
        Gets the deletedDateTime property value. Read only. Timestamp at which the chat message was deleted, or null if not deleted.
        Returns: Optional[datetime]
        """
        return self._deleted_date_time
    
    @deleted_date_time.setter
    def deleted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deletedDateTime property value. Read only. Timestamp at which the chat message was deleted, or null if not deleted.
        Args:
            value: Value to set for the deleted_date_time property.
        """
        self._deleted_date_time = value
    
    @property
    def etag(self,) -> Optional[str]:
        """
        Gets the etag property value. Read-only. Version number of the chat message.
        Returns: Optional[str]
        """
        return self._etag
    
    @etag.setter
    def etag(self,value: Optional[str] = None) -> None:
        """
        Sets the etag property value. Read-only. Version number of the chat message.
        Args:
            value: Value to set for the etag property.
        """
        self._etag = value
    
    @property
    def event_detail(self,) -> Optional[event_message_detail.EventMessageDetail]:
        """
        Gets the eventDetail property value. Read-only. If present, represents details of an event that happened in a chat, a channel, or a team, for example, adding new members. For event messages, the messageType property will be set to systemEventMessage.
        Returns: Optional[event_message_detail.EventMessageDetail]
        """
        return self._event_detail
    
    @event_detail.setter
    def event_detail(self,value: Optional[event_message_detail.EventMessageDetail] = None) -> None:
        """
        Sets the eventDetail property value. Read-only. If present, represents details of an event that happened in a chat, a channel, or a team, for example, adding new members. For event messages, the messageType property will be set to systemEventMessage.
        Args:
            value: Value to set for the event_detail property.
        """
        self._event_detail = value
    
    @property
    def from_(self,) -> Optional[chat_message_from_identity_set.ChatMessageFromIdentitySet]:
        """
        Gets the from property value. Details of the sender of the chat message. Can only be set during migration.
        Returns: Optional[chat_message_from_identity_set.ChatMessageFromIdentitySet]
        """
        return self._from_
    
    @from_.setter
    def from_(self,value: Optional[chat_message_from_identity_set.ChatMessageFromIdentitySet] = None) -> None:
        """
        Sets the from property value. Details of the sender of the chat message. Can only be set during migration.
        Args:
            value: Value to set for the from_ property.
        """
        self._from_ = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import channel_identity, chat_message_attachment, chat_message_from_identity_set, chat_message_history_item, chat_message_hosted_content, chat_message_importance, chat_message_mention, chat_message_policy_violation, chat_message_reaction, chat_message_type, entity, event_message_detail, item_body

        fields: Dict[str, Callable[[Any], None]] = {
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(chat_message_attachment.ChatMessageAttachment)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(item_body.ItemBody)),
            "channelIdentity": lambda n : setattr(self, 'channel_identity', n.get_object_value(channel_identity.ChannelIdentity)),
            "chatId": lambda n : setattr(self, 'chat_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "etag": lambda n : setattr(self, 'etag', n.get_str_value()),
            "eventDetail": lambda n : setattr(self, 'event_detail', n.get_object_value(event_message_detail.EventMessageDetail)),
            "from": lambda n : setattr(self, 'from_', n.get_object_value(chat_message_from_identity_set.ChatMessageFromIdentitySet)),
            "hostedContents": lambda n : setattr(self, 'hosted_contents', n.get_collection_of_object_values(chat_message_hosted_content.ChatMessageHostedContent)),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(chat_message_importance.ChatMessageImportance)),
            "lastEditedDateTime": lambda n : setattr(self, 'last_edited_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "mentions": lambda n : setattr(self, 'mentions', n.get_collection_of_object_values(chat_message_mention.ChatMessageMention)),
            "messageHistory": lambda n : setattr(self, 'message_history', n.get_collection_of_object_values(chat_message_history_item.ChatMessageHistoryItem)),
            "messageType": lambda n : setattr(self, 'message_type', n.get_enum_value(chat_message_type.ChatMessageType)),
            "policyViolation": lambda n : setattr(self, 'policy_violation', n.get_object_value(chat_message_policy_violation.ChatMessagePolicyViolation)),
            "reactions": lambda n : setattr(self, 'reactions', n.get_collection_of_object_values(chat_message_reaction.ChatMessageReaction)),
            "replies": lambda n : setattr(self, 'replies', n.get_collection_of_object_values(ChatMessage)),
            "replyToId": lambda n : setattr(self, 'reply_to_id', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hosted_contents(self,) -> Optional[List[chat_message_hosted_content.ChatMessageHostedContent]]:
        """
        Gets the hostedContents property value. Content in a message hosted by Microsoft Teams - for example, images or code snippets.
        Returns: Optional[List[chat_message_hosted_content.ChatMessageHostedContent]]
        """
        return self._hosted_contents
    
    @hosted_contents.setter
    def hosted_contents(self,value: Optional[List[chat_message_hosted_content.ChatMessageHostedContent]] = None) -> None:
        """
        Sets the hostedContents property value. Content in a message hosted by Microsoft Teams - for example, images or code snippets.
        Args:
            value: Value to set for the hosted_contents property.
        """
        self._hosted_contents = value
    
    @property
    def importance(self,) -> Optional[chat_message_importance.ChatMessageImportance]:
        """
        Gets the importance property value. The importance property
        Returns: Optional[chat_message_importance.ChatMessageImportance]
        """
        return self._importance
    
    @importance.setter
    def importance(self,value: Optional[chat_message_importance.ChatMessageImportance] = None) -> None:
        """
        Sets the importance property value. The importance property
        Args:
            value: Value to set for the importance property.
        """
        self._importance = value
    
    @property
    def last_edited_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastEditedDateTime property value. Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Teams UI. If no edits are made the value is null.
        Returns: Optional[datetime]
        """
        return self._last_edited_date_time
    
    @last_edited_date_time.setter
    def last_edited_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastEditedDateTime property value. Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Teams UI. If no edits are made the value is null.
        Args:
            value: Value to set for the last_edited_date_time property.
        """
        self._last_edited_date_time = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Read only. Timestamp when the chat message is created (initial setting) or modified, including when a reaction is added or removed.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Read only. Timestamp when the chat message is created (initial setting) or modified, including when a reaction is added or removed.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def locale(self,) -> Optional[str]:
        """
        Gets the locale property value. Locale of the chat message set by the client. Always set to en-us.
        Returns: Optional[str]
        """
        return self._locale
    
    @locale.setter
    def locale(self,value: Optional[str] = None) -> None:
        """
        Sets the locale property value. Locale of the chat message set by the client. Always set to en-us.
        Args:
            value: Value to set for the locale property.
        """
        self._locale = value
    
    @property
    def mentions(self,) -> Optional[List[chat_message_mention.ChatMessageMention]]:
        """
        Gets the mentions property value. List of entities mentioned in the chat message. Supported entities are: user, bot, team, and channel.
        Returns: Optional[List[chat_message_mention.ChatMessageMention]]
        """
        return self._mentions
    
    @mentions.setter
    def mentions(self,value: Optional[List[chat_message_mention.ChatMessageMention]] = None) -> None:
        """
        Sets the mentions property value. List of entities mentioned in the chat message. Supported entities are: user, bot, team, and channel.
        Args:
            value: Value to set for the mentions property.
        """
        self._mentions = value
    
    @property
    def message_history(self,) -> Optional[List[chat_message_history_item.ChatMessageHistoryItem]]:
        """
        Gets the messageHistory property value. The messageHistory property
        Returns: Optional[List[chat_message_history_item.ChatMessageHistoryItem]]
        """
        return self._message_history
    
    @message_history.setter
    def message_history(self,value: Optional[List[chat_message_history_item.ChatMessageHistoryItem]] = None) -> None:
        """
        Sets the messageHistory property value. The messageHistory property
        Args:
            value: Value to set for the message_history property.
        """
        self._message_history = value
    
    @property
    def message_type(self,) -> Optional[chat_message_type.ChatMessageType]:
        """
        Gets the messageType property value. The messageType property
        Returns: Optional[chat_message_type.ChatMessageType]
        """
        return self._message_type
    
    @message_type.setter
    def message_type(self,value: Optional[chat_message_type.ChatMessageType] = None) -> None:
        """
        Sets the messageType property value. The messageType property
        Args:
            value: Value to set for the message_type property.
        """
        self._message_type = value
    
    @property
    def policy_violation(self,) -> Optional[chat_message_policy_violation.ChatMessagePolicyViolation]:
        """
        Gets the policyViolation property value. Defines the properties of a policy violation set by a data loss prevention (DLP) application.
        Returns: Optional[chat_message_policy_violation.ChatMessagePolicyViolation]
        """
        return self._policy_violation
    
    @policy_violation.setter
    def policy_violation(self,value: Optional[chat_message_policy_violation.ChatMessagePolicyViolation] = None) -> None:
        """
        Sets the policyViolation property value. Defines the properties of a policy violation set by a data loss prevention (DLP) application.
        Args:
            value: Value to set for the policy_violation property.
        """
        self._policy_violation = value
    
    @property
    def reactions(self,) -> Optional[List[chat_message_reaction.ChatMessageReaction]]:
        """
        Gets the reactions property value. Reactions for this chat message (for example, Like).
        Returns: Optional[List[chat_message_reaction.ChatMessageReaction]]
        """
        return self._reactions
    
    @reactions.setter
    def reactions(self,value: Optional[List[chat_message_reaction.ChatMessageReaction]] = None) -> None:
        """
        Sets the reactions property value. Reactions for this chat message (for example, Like).
        Args:
            value: Value to set for the reactions property.
        """
        self._reactions = value
    
    @property
    def replies(self,) -> Optional[List[ChatMessage]]:
        """
        Gets the replies property value. Replies for a specified message. Supports $expand for channel messages.
        Returns: Optional[List[ChatMessage]]
        """
        return self._replies
    
    @replies.setter
    def replies(self,value: Optional[List[ChatMessage]] = None) -> None:
        """
        Sets the replies property value. Replies for a specified message. Supports $expand for channel messages.
        Args:
            value: Value to set for the replies property.
        """
        self._replies = value
    
    @property
    def reply_to_id(self,) -> Optional[str]:
        """
        Gets the replyToId property value. Read-only. ID of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels, not chats.)
        Returns: Optional[str]
        """
        return self._reply_to_id
    
    @reply_to_id.setter
    def reply_to_id(self,value: Optional[str] = None) -> None:
        """
        Sets the replyToId property value. Read-only. ID of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels, not chats.)
        Args:
            value: Value to set for the reply_to_id property.
        """
        self._reply_to_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject of the chat message, in plaintext.
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject of the chat message, in plaintext.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def summary(self,) -> Optional[str]:
        """
        Gets the summary property value. Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.
        Returns: Optional[str]
        """
        return self._summary
    
    @summary.setter
    def summary(self,value: Optional[str] = None) -> None:
        """
        Sets the summary property value. Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.
        Args:
            value: Value to set for the summary property.
        """
        self._summary = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. Read-only. Link to the message in Microsoft Teams.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. Read-only. Link to the message in Microsoft Teams.
        Args:
            value: Value to set for the web_url property.
        """
        self._web_url = value
    

