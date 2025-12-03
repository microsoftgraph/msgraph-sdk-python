from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .channel_membership_type import ChannelMembershipType
    from .channel_summary import ChannelSummary
    from .chat_message import ChatMessage
    from .conversation_member import ConversationMember
    from .drive_item import DriveItem
    from .entity import Entity
    from .shared_with_channel_team_info import SharedWithChannelTeamInfo
    from .teams_tab import TeamsTab

from .entity import Entity

@dataclass
class Channel(Entity, Parsable):
    # A collection of membership records associated with the channel, including both direct and indirect members of shared channels.
    all_members: Optional[list[ConversationMember]] = None
    # Read only. Timestamp at which the channel was created.
    created_date_time: Optional[datetime.datetime] = None
    # Optional textual description for the channel.
    description: Optional[str] = None
    # Channel name as it will appear to the user in Microsoft Teams. The maximum length is 50 characters.
    display_name: Optional[str] = None
    # The email address for sending messages to the channel. Read-only.
    email: Optional[str] = None
    # Metadata for the location where the channel's files are stored.
    files_folder: Optional[DriveItem] = None
    # Indicates whether the channel is archived. Read-only.
    is_archived: Optional[bool] = None
    # Indicates whether the channel should be marked as recommended for all members of the team to show in their channel list. Note: All recommended channels automatically show in the channels list for education and frontline worker users. The property can only be set programmatically via the Create team method. The default value is false.
    is_favorite_by_default: Optional[bool] = None
    # A collection of membership records associated with the channel.
    members: Optional[list[ConversationMember]] = None
    # The type of the channel. Can be set during creation and can't be changed. The possible values are: standard, private, unknownFutureValue, shared. The default value is standard. Use the Prefer: include-unknown-enum-members request header to get the following members in this evolvable enum: shared.
    membership_type: Optional[ChannelMembershipType] = None
    # A collection of all the messages in the channel. A navigation property. Nullable.
    messages: Optional[list[ChatMessage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of teams with which a channel is shared.
    shared_with_teams: Optional[list[SharedWithChannelTeamInfo]] = None
    # Contains summary information about the channel, including number of owners, members, guests, and an indicator for members from other tenants. The summary property will only be returned if it is specified in the $select clause of the Get channel method.
    summary: Optional[ChannelSummary] = None
    # A collection of all the tabs in the channel. A navigation property.
    tabs: Optional[list[TeamsTab]] = None
    # The ID of the Microsoft Entra tenant.
    tenant_id: Optional[str] = None
    # A hyperlink that will go to the channel in Microsoft Teams. This is the URL that you get when you right-click a channel in Microsoft Teams and select Get link to channel. This URL should be treated as an opaque blob, and not parsed. Read-only.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Channel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Channel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Channel()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .channel_membership_type import ChannelMembershipType
        from .channel_summary import ChannelSummary
        from .chat_message import ChatMessage
        from .conversation_member import ConversationMember
        from .drive_item import DriveItem
        from .entity import Entity
        from .shared_with_channel_team_info import SharedWithChannelTeamInfo
        from .teams_tab import TeamsTab

        from .channel_membership_type import ChannelMembershipType
        from .channel_summary import ChannelSummary
        from .chat_message import ChatMessage
        from .conversation_member import ConversationMember
        from .drive_item import DriveItem
        from .entity import Entity
        from .shared_with_channel_team_info import SharedWithChannelTeamInfo
        from .teams_tab import TeamsTab

        fields: dict[str, Callable[[Any], None]] = {
            "allMembers": lambda n : setattr(self, 'all_members', n.get_collection_of_object_values(ConversationMember)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "filesFolder": lambda n : setattr(self, 'files_folder', n.get_object_value(DriveItem)),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "isFavoriteByDefault": lambda n : setattr(self, 'is_favorite_by_default', n.get_bool_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(ConversationMember)),
            "membershipType": lambda n : setattr(self, 'membership_type', n.get_enum_value(ChannelMembershipType)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(ChatMessage)),
            "sharedWithTeams": lambda n : setattr(self, 'shared_with_teams', n.get_collection_of_object_values(SharedWithChannelTeamInfo)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(ChannelSummary)),
            "tabs": lambda n : setattr(self, 'tabs', n.get_collection_of_object_values(TeamsTab)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("allMembers", self.all_members)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_object_value("filesFolder", self.files_folder)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_bool_value("isFavoriteByDefault", self.is_favorite_by_default)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_enum_value("membershipType", self.membership_type)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_collection_of_object_values("sharedWithTeams", self.shared_with_teams)
        writer.write_object_value("summary", self.summary)
        writer.write_collection_of_object_values("tabs", self.tabs)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("webUrl", self.web_url)
    

