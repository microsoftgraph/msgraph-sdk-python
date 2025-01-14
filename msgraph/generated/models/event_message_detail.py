from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call_ended_event_message_detail import CallEndedEventMessageDetail
    from .call_recording_event_message_detail import CallRecordingEventMessageDetail
    from .call_started_event_message_detail import CallStartedEventMessageDetail
    from .call_transcript_event_message_detail import CallTranscriptEventMessageDetail
    from .channel_added_event_message_detail import ChannelAddedEventMessageDetail
    from .channel_deleted_event_message_detail import ChannelDeletedEventMessageDetail
    from .channel_description_updated_event_message_detail import ChannelDescriptionUpdatedEventMessageDetail
    from .channel_renamed_event_message_detail import ChannelRenamedEventMessageDetail
    from .channel_set_as_favorite_by_default_event_message_detail import ChannelSetAsFavoriteByDefaultEventMessageDetail
    from .channel_unset_as_favorite_by_default_event_message_detail import ChannelUnsetAsFavoriteByDefaultEventMessageDetail
    from .chat_renamed_event_message_detail import ChatRenamedEventMessageDetail
    from .conversation_member_role_updated_event_message_detail import ConversationMemberRoleUpdatedEventMessageDetail
    from .meeting_policy_updated_event_message_detail import MeetingPolicyUpdatedEventMessageDetail
    from .members_added_event_message_detail import MembersAddedEventMessageDetail
    from .members_deleted_event_message_detail import MembersDeletedEventMessageDetail
    from .members_joined_event_message_detail import MembersJoinedEventMessageDetail
    from .members_left_event_message_detail import MembersLeftEventMessageDetail
    from .message_pinned_event_message_detail import MessagePinnedEventMessageDetail
    from .message_unpinned_event_message_detail import MessageUnpinnedEventMessageDetail
    from .tab_updated_event_message_detail import TabUpdatedEventMessageDetail
    from .teams_app_installed_event_message_detail import TeamsAppInstalledEventMessageDetail
    from .teams_app_removed_event_message_detail import TeamsAppRemovedEventMessageDetail
    from .teams_app_upgraded_event_message_detail import TeamsAppUpgradedEventMessageDetail
    from .team_archived_event_message_detail import TeamArchivedEventMessageDetail
    from .team_created_event_message_detail import TeamCreatedEventMessageDetail
    from .team_description_updated_event_message_detail import TeamDescriptionUpdatedEventMessageDetail
    from .team_joining_disabled_event_message_detail import TeamJoiningDisabledEventMessageDetail
    from .team_joining_enabled_event_message_detail import TeamJoiningEnabledEventMessageDetail
    from .team_renamed_event_message_detail import TeamRenamedEventMessageDetail
    from .team_unarchived_event_message_detail import TeamUnarchivedEventMessageDetail

@dataclass
class EventMessageDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EventMessageDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callEndedEventMessageDetail".casefold():
            from .call_ended_event_message_detail import CallEndedEventMessageDetail

            return CallEndedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecordingEventMessageDetail".casefold():
            from .call_recording_event_message_detail import CallRecordingEventMessageDetail

            return CallRecordingEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callStartedEventMessageDetail".casefold():
            from .call_started_event_message_detail import CallStartedEventMessageDetail

            return CallStartedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callTranscriptEventMessageDetail".casefold():
            from .call_transcript_event_message_detail import CallTranscriptEventMessageDetail

            return CallTranscriptEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelAddedEventMessageDetail".casefold():
            from .channel_added_event_message_detail import ChannelAddedEventMessageDetail

            return ChannelAddedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelDeletedEventMessageDetail".casefold():
            from .channel_deleted_event_message_detail import ChannelDeletedEventMessageDetail

            return ChannelDeletedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelDescriptionUpdatedEventMessageDetail".casefold():
            from .channel_description_updated_event_message_detail import ChannelDescriptionUpdatedEventMessageDetail

            return ChannelDescriptionUpdatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelRenamedEventMessageDetail".casefold():
            from .channel_renamed_event_message_detail import ChannelRenamedEventMessageDetail

            return ChannelRenamedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelSetAsFavoriteByDefaultEventMessageDetail".casefold():
            from .channel_set_as_favorite_by_default_event_message_detail import ChannelSetAsFavoriteByDefaultEventMessageDetail

            return ChannelSetAsFavoriteByDefaultEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelUnsetAsFavoriteByDefaultEventMessageDetail".casefold():
            from .channel_unset_as_favorite_by_default_event_message_detail import ChannelUnsetAsFavoriteByDefaultEventMessageDetail

            return ChannelUnsetAsFavoriteByDefaultEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatRenamedEventMessageDetail".casefold():
            from .chat_renamed_event_message_detail import ChatRenamedEventMessageDetail

            return ChatRenamedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conversationMemberRoleUpdatedEventMessageDetail".casefold():
            from .conversation_member_role_updated_event_message_detail import ConversationMemberRoleUpdatedEventMessageDetail

            return ConversationMemberRoleUpdatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingPolicyUpdatedEventMessageDetail".casefold():
            from .meeting_policy_updated_event_message_detail import MeetingPolicyUpdatedEventMessageDetail

            return MeetingPolicyUpdatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.membersAddedEventMessageDetail".casefold():
            from .members_added_event_message_detail import MembersAddedEventMessageDetail

            return MembersAddedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.membersDeletedEventMessageDetail".casefold():
            from .members_deleted_event_message_detail import MembersDeletedEventMessageDetail

            return MembersDeletedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.membersJoinedEventMessageDetail".casefold():
            from .members_joined_event_message_detail import MembersJoinedEventMessageDetail

            return MembersJoinedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.membersLeftEventMessageDetail".casefold():
            from .members_left_event_message_detail import MembersLeftEventMessageDetail

            return MembersLeftEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.messagePinnedEventMessageDetail".casefold():
            from .message_pinned_event_message_detail import MessagePinnedEventMessageDetail

            return MessagePinnedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.messageUnpinnedEventMessageDetail".casefold():
            from .message_unpinned_event_message_detail import MessageUnpinnedEventMessageDetail

            return MessageUnpinnedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tabUpdatedEventMessageDetail".casefold():
            from .tab_updated_event_message_detail import TabUpdatedEventMessageDetail

            return TabUpdatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamArchivedEventMessageDetail".casefold():
            from .team_archived_event_message_detail import TeamArchivedEventMessageDetail

            return TeamArchivedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamCreatedEventMessageDetail".casefold():
            from .team_created_event_message_detail import TeamCreatedEventMessageDetail

            return TeamCreatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamDescriptionUpdatedEventMessageDetail".casefold():
            from .team_description_updated_event_message_detail import TeamDescriptionUpdatedEventMessageDetail

            return TeamDescriptionUpdatedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamJoiningDisabledEventMessageDetail".casefold():
            from .team_joining_disabled_event_message_detail import TeamJoiningDisabledEventMessageDetail

            return TeamJoiningDisabledEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamJoiningEnabledEventMessageDetail".casefold():
            from .team_joining_enabled_event_message_detail import TeamJoiningEnabledEventMessageDetail

            return TeamJoiningEnabledEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamRenamedEventMessageDetail".casefold():
            from .team_renamed_event_message_detail import TeamRenamedEventMessageDetail

            return TeamRenamedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppInstalledEventMessageDetail".casefold():
            from .teams_app_installed_event_message_detail import TeamsAppInstalledEventMessageDetail

            return TeamsAppInstalledEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppRemovedEventMessageDetail".casefold():
            from .teams_app_removed_event_message_detail import TeamsAppRemovedEventMessageDetail

            return TeamsAppRemovedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppUpgradedEventMessageDetail".casefold():
            from .teams_app_upgraded_event_message_detail import TeamsAppUpgradedEventMessageDetail

            return TeamsAppUpgradedEventMessageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamUnarchivedEventMessageDetail".casefold():
            from .team_unarchived_event_message_detail import TeamUnarchivedEventMessageDetail

            return TeamUnarchivedEventMessageDetail()
        return EventMessageDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .call_ended_event_message_detail import CallEndedEventMessageDetail
        from .call_recording_event_message_detail import CallRecordingEventMessageDetail
        from .call_started_event_message_detail import CallStartedEventMessageDetail
        from .call_transcript_event_message_detail import CallTranscriptEventMessageDetail
        from .channel_added_event_message_detail import ChannelAddedEventMessageDetail
        from .channel_deleted_event_message_detail import ChannelDeletedEventMessageDetail
        from .channel_description_updated_event_message_detail import ChannelDescriptionUpdatedEventMessageDetail
        from .channel_renamed_event_message_detail import ChannelRenamedEventMessageDetail
        from .channel_set_as_favorite_by_default_event_message_detail import ChannelSetAsFavoriteByDefaultEventMessageDetail
        from .channel_unset_as_favorite_by_default_event_message_detail import ChannelUnsetAsFavoriteByDefaultEventMessageDetail
        from .chat_renamed_event_message_detail import ChatRenamedEventMessageDetail
        from .conversation_member_role_updated_event_message_detail import ConversationMemberRoleUpdatedEventMessageDetail
        from .meeting_policy_updated_event_message_detail import MeetingPolicyUpdatedEventMessageDetail
        from .members_added_event_message_detail import MembersAddedEventMessageDetail
        from .members_deleted_event_message_detail import MembersDeletedEventMessageDetail
        from .members_joined_event_message_detail import MembersJoinedEventMessageDetail
        from .members_left_event_message_detail import MembersLeftEventMessageDetail
        from .message_pinned_event_message_detail import MessagePinnedEventMessageDetail
        from .message_unpinned_event_message_detail import MessageUnpinnedEventMessageDetail
        from .tab_updated_event_message_detail import TabUpdatedEventMessageDetail
        from .teams_app_installed_event_message_detail import TeamsAppInstalledEventMessageDetail
        from .teams_app_removed_event_message_detail import TeamsAppRemovedEventMessageDetail
        from .teams_app_upgraded_event_message_detail import TeamsAppUpgradedEventMessageDetail
        from .team_archived_event_message_detail import TeamArchivedEventMessageDetail
        from .team_created_event_message_detail import TeamCreatedEventMessageDetail
        from .team_description_updated_event_message_detail import TeamDescriptionUpdatedEventMessageDetail
        from .team_joining_disabled_event_message_detail import TeamJoiningDisabledEventMessageDetail
        from .team_joining_enabled_event_message_detail import TeamJoiningEnabledEventMessageDetail
        from .team_renamed_event_message_detail import TeamRenamedEventMessageDetail
        from .team_unarchived_event_message_detail import TeamUnarchivedEventMessageDetail

        from .call_ended_event_message_detail import CallEndedEventMessageDetail
        from .call_recording_event_message_detail import CallRecordingEventMessageDetail
        from .call_started_event_message_detail import CallStartedEventMessageDetail
        from .call_transcript_event_message_detail import CallTranscriptEventMessageDetail
        from .channel_added_event_message_detail import ChannelAddedEventMessageDetail
        from .channel_deleted_event_message_detail import ChannelDeletedEventMessageDetail
        from .channel_description_updated_event_message_detail import ChannelDescriptionUpdatedEventMessageDetail
        from .channel_renamed_event_message_detail import ChannelRenamedEventMessageDetail
        from .channel_set_as_favorite_by_default_event_message_detail import ChannelSetAsFavoriteByDefaultEventMessageDetail
        from .channel_unset_as_favorite_by_default_event_message_detail import ChannelUnsetAsFavoriteByDefaultEventMessageDetail
        from .chat_renamed_event_message_detail import ChatRenamedEventMessageDetail
        from .conversation_member_role_updated_event_message_detail import ConversationMemberRoleUpdatedEventMessageDetail
        from .meeting_policy_updated_event_message_detail import MeetingPolicyUpdatedEventMessageDetail
        from .members_added_event_message_detail import MembersAddedEventMessageDetail
        from .members_deleted_event_message_detail import MembersDeletedEventMessageDetail
        from .members_joined_event_message_detail import MembersJoinedEventMessageDetail
        from .members_left_event_message_detail import MembersLeftEventMessageDetail
        from .message_pinned_event_message_detail import MessagePinnedEventMessageDetail
        from .message_unpinned_event_message_detail import MessageUnpinnedEventMessageDetail
        from .tab_updated_event_message_detail import TabUpdatedEventMessageDetail
        from .teams_app_installed_event_message_detail import TeamsAppInstalledEventMessageDetail
        from .teams_app_removed_event_message_detail import TeamsAppRemovedEventMessageDetail
        from .teams_app_upgraded_event_message_detail import TeamsAppUpgradedEventMessageDetail
        from .team_archived_event_message_detail import TeamArchivedEventMessageDetail
        from .team_created_event_message_detail import TeamCreatedEventMessageDetail
        from .team_description_updated_event_message_detail import TeamDescriptionUpdatedEventMessageDetail
        from .team_joining_disabled_event_message_detail import TeamJoiningDisabledEventMessageDetail
        from .team_joining_enabled_event_message_detail import TeamJoiningEnabledEventMessageDetail
        from .team_renamed_event_message_detail import TeamRenamedEventMessageDetail
        from .team_unarchived_event_message_detail import TeamUnarchivedEventMessageDetail

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

