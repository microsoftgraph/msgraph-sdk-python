from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audio_conferencing import AudioConferencing
    from .chat_info import ChatInfo
    from .entity import Entity
    from .item_body import ItemBody
    from .join_meeting_id_settings import JoinMeetingIdSettings
    from .lobby_bypass_settings import LobbyBypassSettings
    from .meeting_attendance_report import MeetingAttendanceReport
    from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
    from .meeting_chat_mode import MeetingChatMode
    from .online_meeting import OnlineMeeting
    from .online_meeting_presenters import OnlineMeetingPresenters
    from .virtual_event_session import VirtualEventSession
    from .watermark_protection_values import WatermarkProtectionValues

from .entity import Entity

@dataclass
class OnlineMeetingBase(Entity, Parsable):
    # Indicates whether attendees can turn on their camera.
    allow_attendee_to_enable_camera: Optional[bool] = None
    # Indicates whether attendees can turn on their microphone.
    allow_attendee_to_enable_mic: Optional[bool] = None
    # Specifies the mode of the meeting chat.
    allow_meeting_chat: Optional[MeetingChatMode] = None
    # Specifies if participants are allowed to rename themselves in an instance of the meeting.
    allow_participants_to_change_name: Optional[bool] = None
    # Indicates if Teams reactions are enabled for the meeting.
    allow_teamwork_reactions: Optional[bool] = None
    # Specifies who can be a presenter in a meeting.
    allowed_presenters: Optional[OnlineMeetingPresenters] = None
    # The attendance reports of an online meeting. Read-only.
    attendance_reports: Optional[List[MeetingAttendanceReport]] = None
    # The phone access (dial-in) information for an online meeting. Read-only.
    audio_conferencing: Optional[AudioConferencing] = None
    # The chat information associated with this online meeting.
    chat_info: Optional[ChatInfo] = None
    # Indicates whether to announce when callers join or leave.
    is_entry_exit_announced: Optional[bool] = None
    # The join information in the language and locale variant specified in 'Accept-Language' request HTTP header. Read-only.
    join_information: Optional[ItemBody] = None
    # Specifies the joinMeetingId, the meeting passcode, and the requirement for the passcode. Once an onlineMeeting is created, the joinMeetingIdSettings can't be modified. To make any changes to this property, you must cancel this meeting and create a new one.
    join_meeting_id_settings: Optional[JoinMeetingIdSettings] = None
    # The join URL of the online meeting. Read-only.
    join_web_url: Optional[str] = None
    # Specifies which participants can bypass the meeting lobby.
    lobby_bypass_settings: Optional[LobbyBypassSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether to record the meeting automatically.
    record_automatically: Optional[bool] = None
    # Specifies whether meeting chat history is shared with participants.  Possible values are: all, none, unknownFutureValue.
    share_meeting_chat_history_default: Optional[MeetingChatHistoryDefaultMode] = None
    # The subject of the online meeting.
    subject: Optional[str] = None
    # The video teleconferencing ID. Read-only.
    video_teleconference_id: Optional[str] = None
    # Specifies whether the client application should apply a watermark to a content type.
    watermark_protection: Optional[WatermarkProtectionValues] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnlineMeetingBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeetingBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onlineMeeting".casefold():
            from .online_meeting import OnlineMeeting

            return OnlineMeeting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventSession".casefold():
            from .virtual_event_session import VirtualEventSession

            return VirtualEventSession()
        return OnlineMeetingBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .audio_conferencing import AudioConferencing
        from .chat_info import ChatInfo
        from .entity import Entity
        from .item_body import ItemBody
        from .join_meeting_id_settings import JoinMeetingIdSettings
        from .lobby_bypass_settings import LobbyBypassSettings
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
        from .meeting_chat_mode import MeetingChatMode
        from .online_meeting import OnlineMeeting
        from .online_meeting_presenters import OnlineMeetingPresenters
        from .virtual_event_session import VirtualEventSession
        from .watermark_protection_values import WatermarkProtectionValues

        from .audio_conferencing import AudioConferencing
        from .chat_info import ChatInfo
        from .entity import Entity
        from .item_body import ItemBody
        from .join_meeting_id_settings import JoinMeetingIdSettings
        from .lobby_bypass_settings import LobbyBypassSettings
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
        from .meeting_chat_mode import MeetingChatMode
        from .online_meeting import OnlineMeeting
        from .online_meeting_presenters import OnlineMeetingPresenters
        from .virtual_event_session import VirtualEventSession
        from .watermark_protection_values import WatermarkProtectionValues

        fields: Dict[str, Callable[[Any], None]] = {
            "allowAttendeeToEnableCamera": lambda n : setattr(self, 'allow_attendee_to_enable_camera', n.get_bool_value()),
            "allowAttendeeToEnableMic": lambda n : setattr(self, 'allow_attendee_to_enable_mic', n.get_bool_value()),
            "allowMeetingChat": lambda n : setattr(self, 'allow_meeting_chat', n.get_enum_value(MeetingChatMode)),
            "allowParticipantsToChangeName": lambda n : setattr(self, 'allow_participants_to_change_name', n.get_bool_value()),
            "allowTeamworkReactions": lambda n : setattr(self, 'allow_teamwork_reactions', n.get_bool_value()),
            "allowedPresenters": lambda n : setattr(self, 'allowed_presenters', n.get_enum_value(OnlineMeetingPresenters)),
            "attendanceReports": lambda n : setattr(self, 'attendance_reports', n.get_collection_of_object_values(MeetingAttendanceReport)),
            "audioConferencing": lambda n : setattr(self, 'audio_conferencing', n.get_object_value(AudioConferencing)),
            "chatInfo": lambda n : setattr(self, 'chat_info', n.get_object_value(ChatInfo)),
            "isEntryExitAnnounced": lambda n : setattr(self, 'is_entry_exit_announced', n.get_bool_value()),
            "joinInformation": lambda n : setattr(self, 'join_information', n.get_object_value(ItemBody)),
            "joinMeetingIdSettings": lambda n : setattr(self, 'join_meeting_id_settings', n.get_object_value(JoinMeetingIdSettings)),
            "joinWebUrl": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "lobbyBypassSettings": lambda n : setattr(self, 'lobby_bypass_settings', n.get_object_value(LobbyBypassSettings)),
            "recordAutomatically": lambda n : setattr(self, 'record_automatically', n.get_bool_value()),
            "shareMeetingChatHistoryDefault": lambda n : setattr(self, 'share_meeting_chat_history_default', n.get_enum_value(MeetingChatHistoryDefaultMode)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "videoTeleconferenceId": lambda n : setattr(self, 'video_teleconference_id', n.get_str_value()),
            "watermarkProtection": lambda n : setattr(self, 'watermark_protection', n.get_object_value(WatermarkProtectionValues)),
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
        from .audio_conferencing import AudioConferencing
        from .chat_info import ChatInfo
        from .entity import Entity
        from .item_body import ItemBody
        from .join_meeting_id_settings import JoinMeetingIdSettings
        from .lobby_bypass_settings import LobbyBypassSettings
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
        from .meeting_chat_mode import MeetingChatMode
        from .online_meeting import OnlineMeeting
        from .online_meeting_presenters import OnlineMeetingPresenters
        from .virtual_event_session import VirtualEventSession
        from .watermark_protection_values import WatermarkProtectionValues

        writer.write_bool_value("allowAttendeeToEnableCamera", self.allow_attendee_to_enable_camera)
        writer.write_bool_value("allowAttendeeToEnableMic", self.allow_attendee_to_enable_mic)
        writer.write_enum_value("allowMeetingChat", self.allow_meeting_chat)
        writer.write_bool_value("allowParticipantsToChangeName", self.allow_participants_to_change_name)
        writer.write_bool_value("allowTeamworkReactions", self.allow_teamwork_reactions)
        writer.write_enum_value("allowedPresenters", self.allowed_presenters)
        writer.write_collection_of_object_values("attendanceReports", self.attendance_reports)
        writer.write_object_value("audioConferencing", self.audio_conferencing)
        writer.write_object_value("chatInfo", self.chat_info)
        writer.write_bool_value("isEntryExitAnnounced", self.is_entry_exit_announced)
        writer.write_object_value("joinInformation", self.join_information)
        writer.write_object_value("joinMeetingIdSettings", self.join_meeting_id_settings)
        writer.write_str_value("joinWebUrl", self.join_web_url)
        writer.write_object_value("lobbyBypassSettings", self.lobby_bypass_settings)
        writer.write_bool_value("recordAutomatically", self.record_automatically)
        writer.write_enum_value("shareMeetingChatHistoryDefault", self.share_meeting_chat_history_default)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("videoTeleconferenceId", self.video_teleconference_id)
        writer.write_object_value("watermarkProtection", self.watermark_protection)
    

