from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import chat_message, chat_message_info, chat_type, chat_viewpoint, conversation_member, entity, pinned_chat_message_info, teams_app_installation, teams_tab, teamwork_online_meeting_info

from . import entity

@dataclass
class Chat(entity.Entity):
    # The chatType property
    chat_type: Optional[chat_type.ChatType] = None
    # Date and time at which the chat was created. Read-only.
    created_date_time: Optional[datetime] = None
    # A collection of all the apps in the chat. Nullable.
    installed_apps: Optional[List[teams_app_installation.TeamsAppInstallation]] = None
    # Preview of the last message sent in the chat. Null if no messages have been sent in the chat. Currently, only the list chats operation supports this property.
    last_message_preview: Optional[chat_message_info.ChatMessageInfo] = None
    # Date and time at which the chat was renamed or list of members were last changed. Read-only.
    last_updated_date_time: Optional[datetime] = None
    # A collection of all the members in the chat. Nullable.
    members: Optional[List[conversation_member.ConversationMember]] = None
    # A collection of all the messages in the chat. Nullable.
    messages: Optional[List[chat_message.ChatMessage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents details about an online meeting. If the chat isn't associated with an online meeting, the property is empty. Read-only.
    online_meeting_info: Optional[teamwork_online_meeting_info.TeamworkOnlineMeetingInfo] = None
    # A collection of all the pinned messages in the chat. Nullable.
    pinned_messages: Optional[List[pinned_chat_message_info.PinnedChatMessageInfo]] = None
    # A collection of all the tabs in the chat. Nullable.
    tabs: Optional[List[teams_tab.TeamsTab]] = None
    # The identifier of the tenant in which the chat was created. Read-only.
    tenant_id: Optional[str] = None
    # (Optional) Subject or topic for the chat. Only available for group chats.
    topic: Optional[str] = None
    # Represents caller-specific information about the chat, such as last message read date and time. This property is populated only when the request is made in a delegated context.
    viewpoint: Optional[chat_viewpoint.ChatViewpoint] = None
    # The URL for the chat in Microsoft Teams. The URL should be treated as an opaque blob, and not parsed. Read-only.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Chat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Chat
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Chat()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import chat_message, chat_message_info, chat_type, chat_viewpoint, conversation_member, entity, pinned_chat_message_info, teams_app_installation, teams_tab, teamwork_online_meeting_info

        from . import chat_message, chat_message_info, chat_type, chat_viewpoint, conversation_member, entity, pinned_chat_message_info, teams_app_installation, teams_tab, teamwork_online_meeting_info

        fields: Dict[str, Callable[[Any], None]] = {
            "chatType": lambda n : setattr(self, 'chat_type', n.get_enum_value(chat_type.ChatType)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "installedApps": lambda n : setattr(self, 'installed_apps', n.get_collection_of_object_values(teams_app_installation.TeamsAppInstallation)),
            "lastMessagePreview": lambda n : setattr(self, 'last_message_preview', n.get_object_value(chat_message_info.ChatMessageInfo)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(conversation_member.ConversationMember)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(chat_message.ChatMessage)),
            "onlineMeetingInfo": lambda n : setattr(self, 'online_meeting_info', n.get_object_value(teamwork_online_meeting_info.TeamworkOnlineMeetingInfo)),
            "pinnedMessages": lambda n : setattr(self, 'pinned_messages', n.get_collection_of_object_values(pinned_chat_message_info.PinnedChatMessageInfo)),
            "tabs": lambda n : setattr(self, 'tabs', n.get_collection_of_object_values(teams_tab.TeamsTab)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "topic": lambda n : setattr(self, 'topic', n.get_str_value()),
            "viewpoint": lambda n : setattr(self, 'viewpoint', n.get_object_value(chat_viewpoint.ChatViewpoint)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_enum_value("chatType", self.chat_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("installedApps", self.installed_apps)
        writer.write_object_value("lastMessagePreview", self.last_message_preview)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_object_value("onlineMeetingInfo", self.online_meeting_info)
        writer.write_collection_of_object_values("pinnedMessages", self.pinned_messages)
        writer.write_collection_of_object_values("tabs", self.tabs)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("topic", self.topic)
        writer.write_object_value("viewpoint", self.viewpoint)
        writer.write_str_value("webUrl", self.web_url)
    

