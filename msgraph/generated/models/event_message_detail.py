from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import call_ended_event_message_detail, call_recording_event_message_detail, call_started_event_message_detail, call_transcript_event_message_detail, channel_added_event_message_detail, channel_deleted_event_message_detail, channel_description_updated_event_message_detail, channel_renamed_event_message_detail, channel_set_as_favorite_by_default_event_message_detail, channel_unset_as_favorite_by_default_event_message_detail, chat_renamed_event_message_detail, conversation_member_role_updated_event_message_detail, meeting_policy_updated_event_message_detail, members_added_event_message_detail, members_deleted_event_message_detail, members_joined_event_message_detail, members_left_event_message_detail, message_pinned_event_message_detail, message_unpinned_event_message_detail, tab_updated_event_message_detail, teams_app_installed_event_message_detail, teams_app_removed_event_message_detail, teams_app_upgraded_event_message_detail, team_archived_event_message_detail, team_created_event_message_detail, team_description_updated_event_message_detail, team_joining_disabled_event_message_detail, team_joining_enabled_event_message_detail, team_renamed_event_message_detail, team_unarchived_event_message_detail

@dataclass
class EventMessageDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EventMessageDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callEndedEventMessageDetail".casefold():
            from . import call_ended_event_message_detail

            return call_ended_event_message_detail.CallEndedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecordingEventMessageDetail".casefold():
            from . import call_recording_event_message_detail

            return call_recording_event_message_detail.CallRecordingEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callStartedEventMessageDetail".casefold():
            from . import call_started_event_message_detail

            return call_started_event_message_detail.CallStartedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callTranscriptEventMessageDetail".casefold():
            from . import call_transcript_event_message_detail

            return call_transcript_event_message_detail.CallTranscriptEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelAddedEventMessageDetail".casefold():
            from . import channel_added_event_message_detail

            return channel_added_event_message_detail.ChannelAddedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelDeletedEventMessageDetail".casefold():
            from . import channel_deleted_event_message_detail

            return channel_deleted_event_message_detail.ChannelDeletedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelDescriptionUpdatedEventMessageDetail".casefold():
            from . import channel_description_updated_event_message_detail

            return channel_description_updated_event_message_detail.ChannelDescriptionUpdatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelRenamedEventMessageDetail".casefold():
            from . import channel_renamed_event_message_detail

            return channel_renamed_event_message_detail.ChannelRenamedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelSetAsFavoriteByDefaultEventMessageDetail".casefold():
            from . import channel_set_as_favorite_by_default_event_message_detail

            return channel_set_as_favorite_by_default_event_message_detail.ChannelSetAsFavoriteByDefaultEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelUnsetAsFavoriteByDefaultEventMessageDetail".casefold():
            from . import channel_unset_as_favorite_by_default_event_message_detail

            return channel_unset_as_favorite_by_default_event_message_detail.ChannelUnsetAsFavoriteByDefaultEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatRenamedEventMessageDetail".casefold():
            from . import chat_renamed_event_message_detail

            return chat_renamed_event_message_detail.ChatRenamedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conversationMemberRoleUpdatedEventMessageDetail".casefold():
            from . import conversation_member_role_updated_event_message_detail

            return conversation_member_role_updated_event_message_detail.ConversationMemberRoleUpdatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingPolicyUpdatedEventMessageDetail".casefold():
            from . import meeting_policy_updated_event_message_detail

            return meeting_policy_updated_event_message_detail.MeetingPolicyUpdatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.membersAddedEventMessageDetail".casefold():
            from . import members_added_event_message_detail

            return members_added_event_message_detail.MembersAddedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.membersDeletedEventMessageDetail".casefold():
            from . import members_deleted_event_message_detail

            return members_deleted_event_message_detail.MembersDeletedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.membersJoinedEventMessageDetail".casefold():
            from . import members_joined_event_message_detail

            return members_joined_event_message_detail.MembersJoinedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.membersLeftEventMessageDetail".casefold():
            from . import members_left_event_message_detail

            return members_left_event_message_detail.MembersLeftEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.messagePinnedEventMessageDetail".casefold():
            from . import message_pinned_event_message_detail

            return message_pinned_event_message_detail.MessagePinnedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.messageUnpinnedEventMessageDetail".casefold():
            from . import message_unpinned_event_message_detail

            return message_unpinned_event_message_detail.MessageUnpinnedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tabUpdatedEventMessageDetail".casefold():
            from . import tab_updated_event_message_detail

            return tab_updated_event_message_detail.TabUpdatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamArchivedEventMessageDetail".casefold():
            from . import team_archived_event_message_detail

            return team_archived_event_message_detail.TeamArchivedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamCreatedEventMessageDetail".casefold():
            from . import team_created_event_message_detail

            return team_created_event_message_detail.TeamCreatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamDescriptionUpdatedEventMessageDetail".casefold():
            from . import team_description_updated_event_message_detail

            return team_description_updated_event_message_detail.TeamDescriptionUpdatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamJoiningDisabledEventMessageDetail".casefold():
            from . import team_joining_disabled_event_message_detail

            return team_joining_disabled_event_message_detail.TeamJoiningDisabledEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamJoiningEnabledEventMessageDetail".casefold():
            from . import team_joining_enabled_event_message_detail

            return team_joining_enabled_event_message_detail.TeamJoiningEnabledEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamRenamedEventMessageDetail".casefold():
            from . import team_renamed_event_message_detail

            return team_renamed_event_message_detail.TeamRenamedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppInstalledEventMessageDetail".casefold():
            from . import teams_app_installed_event_message_detail

            return teams_app_installed_event_message_detail.TeamsAppInstalledEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppRemovedEventMessageDetail".casefold():
            from . import teams_app_removed_event_message_detail

            return teams_app_removed_event_message_detail.TeamsAppRemovedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppUpgradedEventMessageDetail".casefold():
            from . import teams_app_upgraded_event_message_detail

            return teams_app_upgraded_event_message_detail.TeamsAppUpgradedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamUnarchivedEventMessageDetail".casefold():
            from . import team_unarchived_event_message_detail

            return team_unarchived_event_message_detail.TeamUnarchivedEventMessageDetail()
        return EventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import call_ended_event_message_detail, call_recording_event_message_detail, call_started_event_message_detail, call_transcript_event_message_detail, channel_added_event_message_detail, channel_deleted_event_message_detail, channel_description_updated_event_message_detail, channel_renamed_event_message_detail, channel_set_as_favorite_by_default_event_message_detail, channel_unset_as_favorite_by_default_event_message_detail, chat_renamed_event_message_detail, conversation_member_role_updated_event_message_detail, meeting_policy_updated_event_message_detail, members_added_event_message_detail, members_deleted_event_message_detail, members_joined_event_message_detail, members_left_event_message_detail, message_pinned_event_message_detail, message_unpinned_event_message_detail, tab_updated_event_message_detail, teams_app_installed_event_message_detail, teams_app_removed_event_message_detail, teams_app_upgraded_event_message_detail, team_archived_event_message_detail, team_created_event_message_detail, team_description_updated_event_message_detail, team_joining_disabled_event_message_detail, team_joining_enabled_event_message_detail, team_renamed_event_message_detail, team_unarchived_event_message_detail

        from . import call_ended_event_message_detail, call_recording_event_message_detail, call_started_event_message_detail, call_transcript_event_message_detail, channel_added_event_message_detail, channel_deleted_event_message_detail, channel_description_updated_event_message_detail, channel_renamed_event_message_detail, channel_set_as_favorite_by_default_event_message_detail, channel_unset_as_favorite_by_default_event_message_detail, chat_renamed_event_message_detail, conversation_member_role_updated_event_message_detail, meeting_policy_updated_event_message_detail, members_added_event_message_detail, members_deleted_event_message_detail, members_joined_event_message_detail, members_left_event_message_detail, message_pinned_event_message_detail, message_unpinned_event_message_detail, tab_updated_event_message_detail, teams_app_installed_event_message_detail, teams_app_removed_event_message_detail, teams_app_upgraded_event_message_detail, team_archived_event_message_detail, team_created_event_message_detail, team_description_updated_event_message_detail, team_joining_disabled_event_message_detail, team_joining_enabled_event_message_detail, team_renamed_event_message_detail, team_unarchived_event_message_detail

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

