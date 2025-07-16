from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .channel import Channel
    from .conversation_member import ConversationMember
    from .entity import Entity
    from .group import Group
    from .profile_photo import ProfilePhoto
    from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
    from .schedule import Schedule
    from .teams_app_installation import TeamsAppInstallation
    from .teams_async_operation import TeamsAsyncOperation
    from .teams_template import TeamsTemplate
    from .teamwork_tag import TeamworkTag
    from .team_fun_settings import TeamFunSettings
    from .team_guest_settings import TeamGuestSettings
    from .team_member_settings import TeamMemberSettings
    from .team_messaging_settings import TeamMessagingSettings
    from .team_specialization import TeamSpecialization
    from .team_summary import TeamSummary
    from .team_visibility_type import TeamVisibilityType

from .entity import Entity

@dataclass
class Team(Entity, Parsable):
    # List of channels either hosted in or shared with the team (incoming channels).
    all_channels: Optional[list[Channel]] = None
    # The collection of channels and messages associated with the team.
    channels: Optional[list[Channel]] = None
    # An optional label. Typically describes the data or business sensitivity of the team. Must match one of a preconfigured set in the tenant's directory.
    classification: Optional[str] = None
    # Timestamp at which the team was created.
    created_date_time: Optional[datetime.datetime] = None
    # An optional description for the team. Maximum length: 1,024 characters.
    description: Optional[str] = None
    # The name of the team.
    display_name: Optional[str] = None
    # The name of the first channel in the team. This is an optional property, only used during team creation and isn't returned in methods to get and list teams.
    first_channel_name: Optional[str] = None
    # Settings to configure use of Giphy, memes, and stickers in the team.
    fun_settings: Optional[TeamFunSettings] = None
    # The group property
    group: Optional[Group] = None
    # Settings to configure whether guests can create, update, or delete channels in the team.
    guest_settings: Optional[TeamGuestSettings] = None
    # List of channels shared with the team.
    incoming_channels: Optional[list[Channel]] = None
    # The apps installed in this team.
    installed_apps: Optional[list[TeamsAppInstallation]] = None
    # A unique ID for the team that was used in a few places such as the audit log/Office 365 Management Activity API.
    internal_id: Optional[str] = None
    # Whether this team is in read-only mode.
    is_archived: Optional[bool] = None
    # Settings to configure whether members can perform certain actions, for example, create channels and add bots, in the team.
    member_settings: Optional[TeamMemberSettings] = None
    # Members and owners of the team.
    members: Optional[list[ConversationMember]] = None
    # Settings to configure messaging and mentions in the team.
    messaging_settings: Optional[TeamMessagingSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The async operations that ran or are running on this team.
    operations: Optional[list[TeamsAsyncOperation]] = None
    # A collection of permissions granted to apps to access the team.
    permission_grants: Optional[list[ResourceSpecificPermissionGrant]] = None
    # The profile photo for the team.
    photo: Optional[ProfilePhoto] = None
    # The general channel for the team.
    primary_channel: Optional[Channel] = None
    # The schedule of shifts for this team.
    schedule: Optional[Schedule] = None
    # Optional. Indicates whether the team is intended for a particular use case. Each team specialization has access to unique behaviors and experiences targeted to its use case.
    specialization: Optional[TeamSpecialization] = None
    # Contains summary information about the team, including number of owners, members, and guests.
    summary: Optional[TeamSummary] = None
    # The tags associated with the team.
    tags: Optional[list[TeamworkTag]] = None
    # The template this team was created from. See available templates.
    template: Optional[TeamsTemplate] = None
    # The ID of the Microsoft Entra tenant.
    tenant_id: Optional[str] = None
    # The visibility of the group and team. Defaults to Public.
    visibility: Optional[TeamVisibilityType] = None
    # A hyperlink that goes to the team in the Microsoft Teams client. You get this URL when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Team:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Team
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Team()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .channel import Channel
        from .conversation_member import ConversationMember
        from .entity import Entity
        from .group import Group
        from .profile_photo import ProfilePhoto
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .schedule import Schedule
        from .teams_app_installation import TeamsAppInstallation
        from .teams_async_operation import TeamsAsyncOperation
        from .teams_template import TeamsTemplate
        from .teamwork_tag import TeamworkTag
        from .team_fun_settings import TeamFunSettings
        from .team_guest_settings import TeamGuestSettings
        from .team_member_settings import TeamMemberSettings
        from .team_messaging_settings import TeamMessagingSettings
        from .team_specialization import TeamSpecialization
        from .team_summary import TeamSummary
        from .team_visibility_type import TeamVisibilityType

        from .channel import Channel
        from .conversation_member import ConversationMember
        from .entity import Entity
        from .group import Group
        from .profile_photo import ProfilePhoto
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .schedule import Schedule
        from .teams_app_installation import TeamsAppInstallation
        from .teams_async_operation import TeamsAsyncOperation
        from .teams_template import TeamsTemplate
        from .teamwork_tag import TeamworkTag
        from .team_fun_settings import TeamFunSettings
        from .team_guest_settings import TeamGuestSettings
        from .team_member_settings import TeamMemberSettings
        from .team_messaging_settings import TeamMessagingSettings
        from .team_specialization import TeamSpecialization
        from .team_summary import TeamSummary
        from .team_visibility_type import TeamVisibilityType

        fields: dict[str, Callable[[Any], None]] = {
            "allChannels": lambda n : setattr(self, 'all_channels', n.get_collection_of_object_values(Channel)),
            "channels": lambda n : setattr(self, 'channels', n.get_collection_of_object_values(Channel)),
            "classification": lambda n : setattr(self, 'classification', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "firstChannelName": lambda n : setattr(self, 'first_channel_name', n.get_str_value()),
            "funSettings": lambda n : setattr(self, 'fun_settings', n.get_object_value(TeamFunSettings)),
            "group": lambda n : setattr(self, 'group', n.get_object_value(Group)),
            "guestSettings": lambda n : setattr(self, 'guest_settings', n.get_object_value(TeamGuestSettings)),
            "incomingChannels": lambda n : setattr(self, 'incoming_channels', n.get_collection_of_object_values(Channel)),
            "installedApps": lambda n : setattr(self, 'installed_apps', n.get_collection_of_object_values(TeamsAppInstallation)),
            "internalId": lambda n : setattr(self, 'internal_id', n.get_str_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "memberSettings": lambda n : setattr(self, 'member_settings', n.get_object_value(TeamMemberSettings)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(ConversationMember)),
            "messagingSettings": lambda n : setattr(self, 'messaging_settings', n.get_object_value(TeamMessagingSettings)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(TeamsAsyncOperation)),
            "permissionGrants": lambda n : setattr(self, 'permission_grants', n.get_collection_of_object_values(ResourceSpecificPermissionGrant)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(ProfilePhoto)),
            "primaryChannel": lambda n : setattr(self, 'primary_channel', n.get_object_value(Channel)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(Schedule)),
            "specialization": lambda n : setattr(self, 'specialization', n.get_enum_value(TeamSpecialization)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(TeamSummary)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(TeamworkTag)),
            "template": lambda n : setattr(self, 'template', n.get_object_value(TeamsTemplate)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(TeamVisibilityType)),
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
        writer.write_collection_of_object_values("allChannels", self.all_channels)
        writer.write_collection_of_object_values("channels", self.channels)
        writer.write_str_value("classification", self.classification)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("firstChannelName", self.first_channel_name)
        writer.write_object_value("funSettings", self.fun_settings)
        writer.write_object_value("group", self.group)
        writer.write_object_value("guestSettings", self.guest_settings)
        writer.write_collection_of_object_values("incomingChannels", self.incoming_channels)
        writer.write_collection_of_object_values("installedApps", self.installed_apps)
        writer.write_str_value("internalId", self.internal_id)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_object_value("memberSettings", self.member_settings)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_object_value("messagingSettings", self.messaging_settings)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("permissionGrants", self.permission_grants)
        writer.write_object_value("photo", self.photo)
        writer.write_object_value("primaryChannel", self.primary_channel)
        writer.write_object_value("schedule", self.schedule)
        writer.write_enum_value("specialization", self.specialization)
        writer.write_object_value("summary", self.summary)
        writer.write_collection_of_object_values("tags", self.tags)
        writer.write_object_value("template", self.template)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_enum_value("visibility", self.visibility)
        writer.write_str_value("webUrl", self.web_url)
    

