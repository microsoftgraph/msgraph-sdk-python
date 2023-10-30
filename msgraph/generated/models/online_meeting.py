from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audio_conferencing import AudioConferencing
    from .broadcast_meeting_settings import BroadcastMeetingSettings
    from .call_transcript import CallTranscript
    from .chat_info import ChatInfo
    from .entity import Entity
    from .item_body import ItemBody
    from .join_meeting_id_settings import JoinMeetingIdSettings
    from .lobby_bypass_settings import LobbyBypassSettings
    from .meeting_attendance_report import MeetingAttendanceReport
    from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
    from .meeting_chat_mode import MeetingChatMode
    from .meeting_participants import MeetingParticipants
    from .online_meeting_presenters import OnlineMeetingPresenters
    from .watermark_protection_values import WatermarkProtectionValues

from .entity import Entity

@dataclass
class OnlineMeeting(Entity):
    # Indicates whether attendees can turn on their camera.
    allow_attendee_to_enable_camera: Optional[bool] = None
    # Indicates whether attendees can turn on their microphone.
    allow_attendee_to_enable_mic: Optional[bool] = None
    # Specifies the mode of meeting chat.
    allow_meeting_chat: Optional[MeetingChatMode] = None
    # Specifies if participants are allowed to rename themselves in an instance of the meeting.
    allow_participants_to_change_name: Optional[bool] = None
    # Indicates whether Teams reactions are enabled for the meeting.
    allow_teamwork_reactions: Optional[bool] = None
    # Specifies who can be a presenter in a meeting. Possible values are listed in the following table.
    allowed_presenters: Optional[OnlineMeetingPresenters] = None
    # The attendance reports of an online meeting. Read-only.
    attendance_reports: Optional[List[MeetingAttendanceReport]] = None
    # The attendeeReport property
    attendee_report: Optional[bytes] = None
    # The phone access (dial-in) information for an online meeting. Read-only.
    audio_conferencing: Optional[AudioConferencing] = None
    # The broadcastSettings property
    broadcast_settings: Optional[BroadcastMeetingSettings] = None
    # The chat information associated with this online meeting.
    chat_info: Optional[ChatInfo] = None
    # The meeting creation time in UTC. Read-only.
    creation_date_time: Optional[datetime.datetime] = None
    # The meeting end time in UTC.
    end_date_time: Optional[datetime.datetime] = None
    # The externalId property
    external_id: Optional[str] = None
    # The isBroadcast property
    is_broadcast: Optional[bool] = None
    # Indicates whether to announce when callers join or leave.
    is_entry_exit_announced: Optional[bool] = None
    # The join information in the language and locale variant specified in the Accept-Language request HTTP header. Read-only.
    join_information: Optional[ItemBody] = None
    # Specifies the joinMeetingId, the meeting passcode, and the requirement for the passcode. Once an onlineMeeting is created, the joinMeetingIdSettings cannot be modified. To make any changes to this property, the meeting needs to be canceled and a new one needs to be created.
    join_meeting_id_settings: Optional[JoinMeetingIdSettings] = None
    # The join URL of the online meeting. Read-only.
    join_web_url: Optional[str] = None
    # Specifies which participants can bypass the meeting   lobby.
    lobby_bypass_settings: Optional[LobbyBypassSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The participants associated with the online meeting.  This includes the organizer and the attendees.
    participants: Optional[MeetingParticipants] = None
    # Indicates whether to record the meeting automatically.
    record_automatically: Optional[bool] = None
    # Specifies whether meeting chat history is shared with participants. Possible values are: all, none, unknownFutureValue.
    share_meeting_chat_history_default: Optional[MeetingChatHistoryDefaultMode] = None
    # The meeting start time in UTC.
    start_date_time: Optional[datetime.datetime] = None
    # The subject of the online meeting.
    subject: Optional[str] = None
    # The transcripts of an online meeting. Read-only.
    transcripts: Optional[List[CallTranscript]] = None
    # The video teleconferencing ID. Read-only.
    video_teleconference_id: Optional[str] = None
    # Specifies whether a watermark should be applied to a content type by the client application.
    watermark_protection: Optional[WatermarkProtectionValues] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnlineMeeting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeeting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnlineMeeting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .audio_conferencing import AudioConferencing
        from .broadcast_meeting_settings import BroadcastMeetingSettings
        from .call_transcript import CallTranscript
        from .chat_info import ChatInfo
        from .entity import Entity
        from .item_body import ItemBody
        from .join_meeting_id_settings import JoinMeetingIdSettings
        from .lobby_bypass_settings import LobbyBypassSettings
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
        from .meeting_chat_mode import MeetingChatMode
        from .meeting_participants import MeetingParticipants
        from .online_meeting_presenters import OnlineMeetingPresenters
        from .watermark_protection_values import WatermarkProtectionValues

        from .audio_conferencing import AudioConferencing
        from .broadcast_meeting_settings import BroadcastMeetingSettings
        from .call_transcript import CallTranscript
        from .chat_info import ChatInfo
        from .entity import Entity
        from .item_body import ItemBody
        from .join_meeting_id_settings import JoinMeetingIdSettings
        from .lobby_bypass_settings import LobbyBypassSettings
        from .meeting_attendance_report import MeetingAttendanceReport
        from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
        from .meeting_chat_mode import MeetingChatMode
        from .meeting_participants import MeetingParticipants
        from .online_meeting_presenters import OnlineMeetingPresenters
        from .watermark_protection_values import WatermarkProtectionValues

        fields: Dict[str, Callable[[Any], None]] = {
            "allow_attendee_to_enable_camera": lambda n : setattr(self, 'allow_attendee_to_enable_camera', n.get_bool_value()),
            "allow_attendee_to_enable_mic": lambda n : setattr(self, 'allow_attendee_to_enable_mic', n.get_bool_value()),
            "allow_meeting_chat": lambda n : setattr(self, 'allow_meeting_chat', n.get_enum_value(MeetingChatMode)),
            "allow_participants_to_change_name": lambda n : setattr(self, 'allow_participants_to_change_name', n.get_bool_value()),
            "allow_teamwork_reactions": lambda n : setattr(self, 'allow_teamwork_reactions', n.get_bool_value()),
            "allowed_presenters": lambda n : setattr(self, 'allowed_presenters', n.get_enum_value(OnlineMeetingPresenters)),
            "attendance_reports": lambda n : setattr(self, 'attendance_reports', n.get_collection_of_object_values(MeetingAttendanceReport)),
            "attendee_report": lambda n : setattr(self, 'attendee_report', n.get_bytes_value()),
            "audio_conferencing": lambda n : setattr(self, 'audio_conferencing', n.get_object_value(AudioConferencing)),
            "broadcast_settings": lambda n : setattr(self, 'broadcast_settings', n.get_object_value(BroadcastMeetingSettings)),
            "chat_info": lambda n : setattr(self, 'chat_info', n.get_object_value(ChatInfo)),
            "creation_date_time": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "is_broadcast": lambda n : setattr(self, 'is_broadcast', n.get_bool_value()),
            "is_entry_exit_announced": lambda n : setattr(self, 'is_entry_exit_announced', n.get_bool_value()),
            "join_information": lambda n : setattr(self, 'join_information', n.get_object_value(ItemBody)),
            "join_meeting_id_settings": lambda n : setattr(self, 'join_meeting_id_settings', n.get_object_value(JoinMeetingIdSettings)),
            "join_web_url": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "lobby_bypass_settings": lambda n : setattr(self, 'lobby_bypass_settings', n.get_object_value(LobbyBypassSettings)),
            "participants": lambda n : setattr(self, 'participants', n.get_object_value(MeetingParticipants)),
            "record_automatically": lambda n : setattr(self, 'record_automatically', n.get_bool_value()),
            "share_meeting_chat_history_default": lambda n : setattr(self, 'share_meeting_chat_history_default', n.get_enum_value(MeetingChatHistoryDefaultMode)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "transcripts": lambda n : setattr(self, 'transcripts', n.get_collection_of_object_values(CallTranscript)),
            "video_teleconference_id": lambda n : setattr(self, 'video_teleconference_id', n.get_str_value()),
            "watermark_protection": lambda n : setattr(self, 'watermark_protection', n.get_object_value(WatermarkProtectionValues)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("allow_attendee_to_enable_camera", self.allow_attendee_to_enable_camera)
        writer.write_bool_value("allow_attendee_to_enable_mic", self.allow_attendee_to_enable_mic)
        writer.write_enum_value("allow_meeting_chat", self.allow_meeting_chat)
        writer.write_bool_value("allow_participants_to_change_name", self.allow_participants_to_change_name)
        writer.write_bool_value("allow_teamwork_reactions", self.allow_teamwork_reactions)
        writer.write_enum_value("allowed_presenters", self.allowed_presenters)
        writer.write_collection_of_object_values("attendance_reports", self.attendance_reports)
        writer.write_bytes_value("attendee_report", self.attendee_report)
        writer.write_object_value("audio_conferencing", self.audio_conferencing)
        writer.write_object_value("broadcast_settings", self.broadcast_settings)
        writer.write_object_value("chat_info", self.chat_info)
        writer.write_datetime_value("creation_date_time", self.creation_date_time)
        writer.write_datetime_value("end_date_time", self.end_date_time)
        writer.write_str_value("external_id", self.external_id)
        writer.write_bool_value("is_broadcast", self.is_broadcast)
        writer.write_bool_value("is_entry_exit_announced", self.is_entry_exit_announced)
        writer.write_object_value("join_information", self.join_information)
        writer.write_object_value("join_meeting_id_settings", self.join_meeting_id_settings)
        writer.write_str_value("join_web_url", self.join_web_url)
        writer.write_object_value("lobby_bypass_settings", self.lobby_bypass_settings)
        writer.write_object_value("participants", self.participants)
        writer.write_bool_value("record_automatically", self.record_automatically)
        writer.write_enum_value("share_meeting_chat_history_default", self.share_meeting_chat_history_default)
        writer.write_datetime_value("start_date_time", self.start_date_time)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_object_values("transcripts", self.transcripts)
        writer.write_str_value("video_teleconference_id", self.video_teleconference_id)
        writer.write_object_value("watermark_protection", self.watermark_protection)
    

