from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_message import ChatMessage
    from .chat_message_info import ChatMessageInfo
    from .chat_type import ChatType
    from .chat_viewpoint import ChatViewpoint
    from .conversation_member import ConversationMember
    from .entity import Entity
    from .pinned_chat_message_info import PinnedChatMessageInfo
    from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
    from .teams_app_installation import TeamsAppInstallation
    from .teams_tab import TeamsTab
    from .teamwork_online_meeting_info import TeamworkOnlineMeetingInfo

from .entity import Entity

@dataclass
class Chat(Entity, Parsable):
    # The chatType property
    chat_type: Optional[ChatType] = None
    # Date and time at which the chat was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # A collection of all the apps in the chat. Nullable.
    installed_apps: Optional[list[TeamsAppInstallation]] = None
    # Indicates whether the chat is hidden for all its members. Read-only.
    is_hidden_for_all_members: Optional[bool] = None
    # Preview of the last message sent in the chat. Null if no messages were sent in the chat. Currently, only the list chats operation supports this property.
    last_message_preview: Optional[ChatMessageInfo] = None
    # Date and time at which the chat was renamed or the list of members was last changed. Read-only.
    last_updated_date_time: Optional[datetime.datetime] = None
    # A collection of all the members in the chat. Nullable.
    members: Optional[list[ConversationMember]] = None
    # A collection of all the messages in the chat. Nullable.
    messages: Optional[list[ChatMessage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents details about an online meeting. If the chat isn't associated with an online meeting, the property is empty. Read-only.
    online_meeting_info: Optional[TeamworkOnlineMeetingInfo] = None
    # A collection of permissions granted to apps for the chat.
    permission_grants: Optional[list[ResourceSpecificPermissionGrant]] = None
    # A collection of all the pinned messages in the chat. Nullable.
    pinned_messages: Optional[list[PinnedChatMessageInfo]] = None
    # A collection of all the tabs in the chat. Nullable.
    tabs: Optional[list[TeamsTab]] = None
    # The identifier of the tenant in which the chat was created. Read-only.
    tenant_id: Optional[str] = None
    # (Optional) Subject or topic for the chat. Only available for group chats.
    topic: Optional[str] = None
    # Represents caller-specific information about the chat, such as the last message read date and time. This property is populated only when the request is made in a delegated context.
    viewpoint: Optional[ChatViewpoint] = None
    # The URL for the chat in Microsoft Teams. The URL should be treated as an opaque blob, and not parsed. Read-only.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Chat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Chat
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Chat()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chat_message import ChatMessage
        from .chat_message_info import ChatMessageInfo
        from .chat_type import ChatType
        from .chat_viewpoint import ChatViewpoint
        from .conversation_member import ConversationMember
        from .entity import Entity
        from .pinned_chat_message_info import PinnedChatMessageInfo
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .teams_app_installation import TeamsAppInstallation
        from .teams_tab import TeamsTab
        from .teamwork_online_meeting_info import TeamworkOnlineMeetingInfo

        from .chat_message import ChatMessage
        from .chat_message_info import ChatMessageInfo
        from .chat_type import ChatType
        from .chat_viewpoint import ChatViewpoint
        from .conversation_member import ConversationMember
        from .entity import Entity
        from .pinned_chat_message_info import PinnedChatMessageInfo
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .teams_app_installation import TeamsAppInstallation
        from .teams_tab import TeamsTab
        from .teamwork_online_meeting_info import TeamworkOnlineMeetingInfo

        fields: dict[str, Callable[[Any], None]] = {
            "chatType": lambda n : setattr(self, 'chat_type', n.get_enum_value(ChatType)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "installedApps": lambda n : setattr(self, 'installed_apps', n.get_collection_of_object_values(TeamsAppInstallation)),
            "isHiddenForAllMembers": lambda n : setattr(self, 'is_hidden_for_all_members', n.get_bool_value()),
            "lastMessagePreview": lambda n : setattr(self, 'last_message_preview', n.get_object_value(ChatMessageInfo)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(ConversationMember)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(ChatMessage)),
            "onlineMeetingInfo": lambda n : setattr(self, 'online_meeting_info', n.get_object_value(TeamworkOnlineMeetingInfo)),
            "permissionGrants": lambda n : setattr(self, 'permission_grants', n.get_collection_of_object_values(ResourceSpecificPermissionGrant)),
            "pinnedMessages": lambda n : setattr(self, 'pinned_messages', n.get_collection_of_object_values(PinnedChatMessageInfo)),
            "tabs": lambda n : setattr(self, 'tabs', n.get_collection_of_object_values(TeamsTab)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "topic": lambda n : setattr(self, 'topic', n.get_str_value()),
            "viewpoint": lambda n : setattr(self, 'viewpoint', n.get_object_value(ChatViewpoint)),
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
        writer.write_enum_value("chatType", self.chat_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("installedApps", self.installed_apps)
        writer.write_bool_value("isHiddenForAllMembers", self.is_hidden_for_all_members)
        writer.write_object_value("lastMessagePreview", self.last_message_preview)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_object_value("onlineMeetingInfo", self.online_meeting_info)
        writer.write_collection_of_object_values("permissionGrants", self.permission_grants)
        writer.write_collection_of_object_values("pinnedMessages", self.pinned_messages)
        writer.write_collection_of_object_values("tabs", self.tabs)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("topic", self.topic)
        writer.write_object_value("viewpoint", self.viewpoint)
        writer.write_str_value("webUrl", self.web_url)
    

