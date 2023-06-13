from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import channel, conversation_member, entity, group, profile_photo, schedule, teams_app_installation, teams_async_operation, teams_template, teamwork_tag, team_fun_settings, team_guest_settings, team_member_settings, team_messaging_settings, team_specialization, team_summary, team_visibility_type

from . import entity

@dataclass
class Team(entity.Entity):
    # List of channels either hosted in or shared with the team (incoming channels).
    all_channels: Optional[List[channel.Channel]] = None
    # The collection of channels and messages associated with the team.
    channels: Optional[List[channel.Channel]] = None
    # An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.
    classification: Optional[str] = None
    # Timestamp at which the team was created.
    created_date_time: Optional[datetime] = None
    # An optional description for the team. Maximum length: 1024 characters.
    description: Optional[str] = None
    # The name of the team.
    display_name: Optional[str] = None
    # Settings to configure use of Giphy, memes, and stickers in the team.
    fun_settings: Optional[team_fun_settings.TeamFunSettings] = None
    # The group property
    group: Optional[group.Group] = None
    # Settings to configure whether guests can create, update, or delete channels in the team.
    guest_settings: Optional[team_guest_settings.TeamGuestSettings] = None
    # List of channels shared with the team.
    incoming_channels: Optional[List[channel.Channel]] = None
    # The apps installed in this team.
    installed_apps: Optional[List[teams_app_installation.TeamsAppInstallation]] = None
    # A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.
    internal_id: Optional[str] = None
    # Whether this team is in read-only mode.
    is_archived: Optional[bool] = None
    # Settings to configure whether members can perform certain actions, for example, create channels and add bots, in the team.
    member_settings: Optional[team_member_settings.TeamMemberSettings] = None
    # Members and owners of the team.
    members: Optional[List[conversation_member.ConversationMember]] = None
    # Settings to configure messaging and mentions in the team.
    messaging_settings: Optional[team_messaging_settings.TeamMessagingSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The async operations that ran or are running on this team.
    operations: Optional[List[teams_async_operation.TeamsAsyncOperation]] = None
    # The profile photo for the team.
    photo: Optional[profile_photo.ProfilePhoto] = None
    # The general channel for the team.
    primary_channel: Optional[channel.Channel] = None
    # The schedule of shifts for this team.
    schedule: Optional[schedule.Schedule] = None
    # Optional. Indicates whether the team is intended for a particular use case.  Each team specialization has access to unique behaviors and experiences targeted to its use case.
    specialization: Optional[team_specialization.TeamSpecialization] = None
    # Contains summary information about the team, including number of owners, members, and guests.
    summary: Optional[team_summary.TeamSummary] = None
    # The tags associated with the team.
    tags: Optional[List[teamwork_tag.TeamworkTag]] = None
    # The template this team was created from. See available templates.
    template: Optional[teams_template.TeamsTemplate] = None
    # The ID of the Azure Active Directory tenant.
    tenant_id: Optional[str] = None
    # The visibility of the group and team. Defaults to Public.
    visibility: Optional[team_visibility_type.TeamVisibilityType] = None
    # A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Team:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Team
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Team()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import channel, conversation_member, entity, group, profile_photo, schedule, teams_app_installation, teams_async_operation, teams_template, teamwork_tag, team_fun_settings, team_guest_settings, team_member_settings, team_messaging_settings, team_specialization, team_summary, team_visibility_type

        fields: Dict[str, Callable[[Any], None]] = {
            "allChannels": lambda n : setattr(self, 'all_channels', n.get_collection_of_object_values(channel.Channel)),
            "channels": lambda n : setattr(self, 'channels', n.get_collection_of_object_values(channel.Channel)),
            "classification": lambda n : setattr(self, 'classification', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "funSettings": lambda n : setattr(self, 'fun_settings', n.get_object_value(team_fun_settings.TeamFunSettings)),
            "group": lambda n : setattr(self, 'group', n.get_object_value(group.Group)),
            "guestSettings": lambda n : setattr(self, 'guest_settings', n.get_object_value(team_guest_settings.TeamGuestSettings)),
            "incomingChannels": lambda n : setattr(self, 'incoming_channels', n.get_collection_of_object_values(channel.Channel)),
            "installedApps": lambda n : setattr(self, 'installed_apps', n.get_collection_of_object_values(teams_app_installation.TeamsAppInstallation)),
            "internalId": lambda n : setattr(self, 'internal_id', n.get_str_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(conversation_member.ConversationMember)),
            "memberSettings": lambda n : setattr(self, 'member_settings', n.get_object_value(team_member_settings.TeamMemberSettings)),
            "messagingSettings": lambda n : setattr(self, 'messaging_settings', n.get_object_value(team_messaging_settings.TeamMessagingSettings)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(teams_async_operation.TeamsAsyncOperation)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(profile_photo.ProfilePhoto)),
            "primaryChannel": lambda n : setattr(self, 'primary_channel', n.get_object_value(channel.Channel)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(schedule.Schedule)),
            "specialization": lambda n : setattr(self, 'specialization', n.get_enum_value(team_specialization.TeamSpecialization)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(team_summary.TeamSummary)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(teamwork_tag.TeamworkTag)),
            "template": lambda n : setattr(self, 'template', n.get_object_value(teams_template.TeamsTemplate)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(team_visibility_type.TeamVisibilityType)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("allChannels", self.all_channels)
        writer.write_collection_of_object_values("channels", self.channels)
        writer.write_str_value("classification", self.classification)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("funSettings", self.fun_settings)
        writer.write_object_value("group", self.group)
        writer.write_object_value("guestSettings", self.guest_settings)
        writer.write_collection_of_object_values("incomingChannels", self.incoming_channels)
        writer.write_collection_of_object_values("installedApps", self.installed_apps)
        writer.write_str_value("internalId", self.internal_id)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_object_value("memberSettings", self.member_settings)
        writer.write_object_value("messagingSettings", self.messaging_settings)
        writer.write_collection_of_object_values("operations", self.operations)
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
    

