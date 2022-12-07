from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

audio_conferencing = lazy_import('msgraph.generated.models.audio_conferencing')
broadcast_meeting_settings = lazy_import('msgraph.generated.models.broadcast_meeting_settings')
chat_info = lazy_import('msgraph.generated.models.chat_info')
entity = lazy_import('msgraph.generated.models.entity')
item_body = lazy_import('msgraph.generated.models.item_body')
lobby_bypass_settings = lazy_import('msgraph.generated.models.lobby_bypass_settings')
meeting_attendance_report = lazy_import('msgraph.generated.models.meeting_attendance_report')
meeting_chat_mode = lazy_import('msgraph.generated.models.meeting_chat_mode')
meeting_participants = lazy_import('msgraph.generated.models.meeting_participants')
online_meeting_presenters = lazy_import('msgraph.generated.models.online_meeting_presenters')

class OnlineMeeting(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def allow_attendee_to_enable_camera(self,) -> Optional[bool]:
        """
        Gets the allowAttendeeToEnableCamera property value. Indicates whether attendees can turn on their camera.
        Returns: Optional[bool]
        """
        return self._allow_attendee_to_enable_camera
    
    @allow_attendee_to_enable_camera.setter
    def allow_attendee_to_enable_camera(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowAttendeeToEnableCamera property value. Indicates whether attendees can turn on their camera.
        Args:
            value: Value to set for the allowAttendeeToEnableCamera property.
        """
        self._allow_attendee_to_enable_camera = value
    
    @property
    def allow_attendee_to_enable_mic(self,) -> Optional[bool]:
        """
        Gets the allowAttendeeToEnableMic property value. Indicates whether attendees can turn on their microphone.
        Returns: Optional[bool]
        """
        return self._allow_attendee_to_enable_mic
    
    @allow_attendee_to_enable_mic.setter
    def allow_attendee_to_enable_mic(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowAttendeeToEnableMic property value. Indicates whether attendees can turn on their microphone.
        Args:
            value: Value to set for the allowAttendeeToEnableMic property.
        """
        self._allow_attendee_to_enable_mic = value
    
    @property
    def allowed_presenters(self,) -> Optional[online_meeting_presenters.OnlineMeetingPresenters]:
        """
        Gets the allowedPresenters property value. Specifies who can be a presenter in a meeting. Possible values are listed in the following table.
        Returns: Optional[online_meeting_presenters.OnlineMeetingPresenters]
        """
        return self._allowed_presenters
    
    @allowed_presenters.setter
    def allowed_presenters(self,value: Optional[online_meeting_presenters.OnlineMeetingPresenters] = None) -> None:
        """
        Sets the allowedPresenters property value. Specifies who can be a presenter in a meeting. Possible values are listed in the following table.
        Args:
            value: Value to set for the allowedPresenters property.
        """
        self._allowed_presenters = value
    
    @property
    def allow_meeting_chat(self,) -> Optional[meeting_chat_mode.MeetingChatMode]:
        """
        Gets the allowMeetingChat property value. Specifies the mode of meeting chat.
        Returns: Optional[meeting_chat_mode.MeetingChatMode]
        """
        return self._allow_meeting_chat
    
    @allow_meeting_chat.setter
    def allow_meeting_chat(self,value: Optional[meeting_chat_mode.MeetingChatMode] = None) -> None:
        """
        Sets the allowMeetingChat property value. Specifies the mode of meeting chat.
        Args:
            value: Value to set for the allowMeetingChat property.
        """
        self._allow_meeting_chat = value
    
    @property
    def allow_teamwork_reactions(self,) -> Optional[bool]:
        """
        Gets the allowTeamworkReactions property value. Indicates whether Teams reactions are enabled for the meeting.
        Returns: Optional[bool]
        """
        return self._allow_teamwork_reactions
    
    @allow_teamwork_reactions.setter
    def allow_teamwork_reactions(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowTeamworkReactions property value. Indicates whether Teams reactions are enabled for the meeting.
        Args:
            value: Value to set for the allowTeamworkReactions property.
        """
        self._allow_teamwork_reactions = value
    
    @property
    def attendance_reports(self,) -> Optional[List[meeting_attendance_report.MeetingAttendanceReport]]:
        """
        Gets the attendanceReports property value. The attendance reports of an online meeting. Read-only.
        Returns: Optional[List[meeting_attendance_report.MeetingAttendanceReport]]
        """
        return self._attendance_reports
    
    @attendance_reports.setter
    def attendance_reports(self,value: Optional[List[meeting_attendance_report.MeetingAttendanceReport]] = None) -> None:
        """
        Sets the attendanceReports property value. The attendance reports of an online meeting. Read-only.
        Args:
            value: Value to set for the attendanceReports property.
        """
        self._attendance_reports = value
    
    @property
    def attendee_report(self,) -> Optional[bytes]:
        """
        Gets the attendeeReport property value. The content stream of the attendee report of a Microsoft Teams live event. Read-only.
        Returns: Optional[bytes]
        """
        return self._attendee_report
    
    @attendee_report.setter
    def attendee_report(self,value: Optional[bytes] = None) -> None:
        """
        Sets the attendeeReport property value. The content stream of the attendee report of a Microsoft Teams live event. Read-only.
        Args:
            value: Value to set for the attendeeReport property.
        """
        self._attendee_report = value
    
    @property
    def audio_conferencing(self,) -> Optional[audio_conferencing.AudioConferencing]:
        """
        Gets the audioConferencing property value. The phone access (dial-in) information for an online meeting. Read-only.
        Returns: Optional[audio_conferencing.AudioConferencing]
        """
        return self._audio_conferencing
    
    @audio_conferencing.setter
    def audio_conferencing(self,value: Optional[audio_conferencing.AudioConferencing] = None) -> None:
        """
        Sets the audioConferencing property value. The phone access (dial-in) information for an online meeting. Read-only.
        Args:
            value: Value to set for the audioConferencing property.
        """
        self._audio_conferencing = value
    
    @property
    def broadcast_settings(self,) -> Optional[broadcast_meeting_settings.BroadcastMeetingSettings]:
        """
        Gets the broadcastSettings property value. Settings related to a live event.
        Returns: Optional[broadcast_meeting_settings.BroadcastMeetingSettings]
        """
        return self._broadcast_settings
    
    @broadcast_settings.setter
    def broadcast_settings(self,value: Optional[broadcast_meeting_settings.BroadcastMeetingSettings] = None) -> None:
        """
        Sets the broadcastSettings property value. Settings related to a live event.
        Args:
            value: Value to set for the broadcastSettings property.
        """
        self._broadcast_settings = value
    
    @property
    def chat_info(self,) -> Optional[chat_info.ChatInfo]:
        """
        Gets the chatInfo property value. The chat information associated with this online meeting.
        Returns: Optional[chat_info.ChatInfo]
        """
        return self._chat_info
    
    @chat_info.setter
    def chat_info(self,value: Optional[chat_info.ChatInfo] = None) -> None:
        """
        Sets the chatInfo property value. The chat information associated with this online meeting.
        Args:
            value: Value to set for the chatInfo property.
        """
        self._chat_info = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new onlineMeeting and sets the default values.
        """
        super().__init__()
        # Indicates whether attendees can turn on their camera.
        self._allow_attendee_to_enable_camera: Optional[bool] = None
        # Indicates whether attendees can turn on their microphone.
        self._allow_attendee_to_enable_mic: Optional[bool] = None
        # Specifies who can be a presenter in a meeting. Possible values are listed in the following table.
        self._allowed_presenters: Optional[online_meeting_presenters.OnlineMeetingPresenters] = None
        # Specifies the mode of meeting chat.
        self._allow_meeting_chat: Optional[meeting_chat_mode.MeetingChatMode] = None
        # Indicates whether Teams reactions are enabled for the meeting.
        self._allow_teamwork_reactions: Optional[bool] = None
        # The attendance reports of an online meeting. Read-only.
        self._attendance_reports: Optional[List[meeting_attendance_report.MeetingAttendanceReport]] = None
        # The content stream of the attendee report of a Microsoft Teams live event. Read-only.
        self._attendee_report: Optional[bytes] = None
        # The phone access (dial-in) information for an online meeting. Read-only.
        self._audio_conferencing: Optional[audio_conferencing.AudioConferencing] = None
        # Settings related to a live event.
        self._broadcast_settings: Optional[broadcast_meeting_settings.BroadcastMeetingSettings] = None
        # The chat information associated with this online meeting.
        self._chat_info: Optional[chat_info.ChatInfo] = None
        # The meeting creation time in UTC. Read-only.
        self._creation_date_time: Optional[datetime] = None
        # The meeting end time in UTC.
        self._end_date_time: Optional[datetime] = None
        # The externalId property
        self._external_id: Optional[str] = None
        # Indicates if this is a Teams live event.
        self._is_broadcast: Optional[bool] = None
        # Indicates whether to announce when callers join or leave.
        self._is_entry_exit_announced: Optional[bool] = None
        # The join information in the language and locale variant specified in the Accept-Language request HTTP header. Read-only.
        self._join_information: Optional[item_body.ItemBody] = None
        # The join URL of the online meeting. Read-only.
        self._join_web_url: Optional[str] = None
        # Specifies which participants can bypass the meeting   lobby.
        self._lobby_bypass_settings: Optional[lobby_bypass_settings.LobbyBypassSettings] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The participants associated with the online meeting.  This includes the organizer and the attendees.
        self._participants: Optional[meeting_participants.MeetingParticipants] = None
        # Indicates whether to record the meeting automatically.
        self._record_automatically: Optional[bool] = None
        # The meeting start time in UTC.
        self._start_date_time: Optional[datetime] = None
        # The subject of the online meeting.
        self._subject: Optional[str] = None
        # The video teleconferencing ID. Read-only.
        self._video_teleconference_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnlineMeeting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeeting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnlineMeeting()
    
    @property
    def creation_date_time(self,) -> Optional[datetime]:
        """
        Gets the creationDateTime property value. The meeting creation time in UTC. Read-only.
        Returns: Optional[datetime]
        """
        return self._creation_date_time
    
    @creation_date_time.setter
    def creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the creationDateTime property value. The meeting creation time in UTC. Read-only.
        Args:
            value: Value to set for the creationDateTime property.
        """
        self._creation_date_time = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The meeting end time in UTC.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The meeting end time in UTC.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. The externalId property
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. The externalId property
        Args:
            value: Value to set for the externalId property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_attendee_to_enable_camera": lambda n : setattr(self, 'allow_attendee_to_enable_camera', n.get_bool_value()),
            "allow_attendee_to_enable_mic": lambda n : setattr(self, 'allow_attendee_to_enable_mic', n.get_bool_value()),
            "allowed_presenters": lambda n : setattr(self, 'allowed_presenters', n.get_enum_value(online_meeting_presenters.OnlineMeetingPresenters)),
            "allow_meeting_chat": lambda n : setattr(self, 'allow_meeting_chat', n.get_enum_value(meeting_chat_mode.MeetingChatMode)),
            "allow_teamwork_reactions": lambda n : setattr(self, 'allow_teamwork_reactions', n.get_bool_value()),
            "attendance_reports": lambda n : setattr(self, 'attendance_reports', n.get_collection_of_object_values(meeting_attendance_report.MeetingAttendanceReport)),
            "attendee_report": lambda n : setattr(self, 'attendee_report', n.get_bytes_value()),
            "audio_conferencing": lambda n : setattr(self, 'audio_conferencing', n.get_object_value(audio_conferencing.AudioConferencing)),
            "broadcast_settings": lambda n : setattr(self, 'broadcast_settings', n.get_object_value(broadcast_meeting_settings.BroadcastMeetingSettings)),
            "chat_info": lambda n : setattr(self, 'chat_info', n.get_object_value(chat_info.ChatInfo)),
            "creation_date_time": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "is_broadcast": lambda n : setattr(self, 'is_broadcast', n.get_bool_value()),
            "is_entry_exit_announced": lambda n : setattr(self, 'is_entry_exit_announced', n.get_bool_value()),
            "join_information": lambda n : setattr(self, 'join_information', n.get_object_value(item_body.ItemBody)),
            "join_web_url": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "lobby_bypass_settings": lambda n : setattr(self, 'lobby_bypass_settings', n.get_object_value(lobby_bypass_settings.LobbyBypassSettings)),
            "participants": lambda n : setattr(self, 'participants', n.get_object_value(meeting_participants.MeetingParticipants)),
            "record_automatically": lambda n : setattr(self, 'record_automatically', n.get_bool_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "video_teleconference_id": lambda n : setattr(self, 'video_teleconference_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_broadcast(self,) -> Optional[bool]:
        """
        Gets the isBroadcast property value. Indicates if this is a Teams live event.
        Returns: Optional[bool]
        """
        return self._is_broadcast
    
    @is_broadcast.setter
    def is_broadcast(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBroadcast property value. Indicates if this is a Teams live event.
        Args:
            value: Value to set for the isBroadcast property.
        """
        self._is_broadcast = value
    
    @property
    def is_entry_exit_announced(self,) -> Optional[bool]:
        """
        Gets the isEntryExitAnnounced property value. Indicates whether to announce when callers join or leave.
        Returns: Optional[bool]
        """
        return self._is_entry_exit_announced
    
    @is_entry_exit_announced.setter
    def is_entry_exit_announced(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEntryExitAnnounced property value. Indicates whether to announce when callers join or leave.
        Args:
            value: Value to set for the isEntryExitAnnounced property.
        """
        self._is_entry_exit_announced = value
    
    @property
    def join_information(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the joinInformation property value. The join information in the language and locale variant specified in the Accept-Language request HTTP header. Read-only.
        Returns: Optional[item_body.ItemBody]
        """
        return self._join_information
    
    @join_information.setter
    def join_information(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the joinInformation property value. The join information in the language and locale variant specified in the Accept-Language request HTTP header. Read-only.
        Args:
            value: Value to set for the joinInformation property.
        """
        self._join_information = value
    
    @property
    def join_web_url(self,) -> Optional[str]:
        """
        Gets the joinWebUrl property value. The join URL of the online meeting. Read-only.
        Returns: Optional[str]
        """
        return self._join_web_url
    
    @join_web_url.setter
    def join_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the joinWebUrl property value. The join URL of the online meeting. Read-only.
        Args:
            value: Value to set for the joinWebUrl property.
        """
        self._join_web_url = value
    
    @property
    def lobby_bypass_settings(self,) -> Optional[lobby_bypass_settings.LobbyBypassSettings]:
        """
        Gets the lobbyBypassSettings property value. Specifies which participants can bypass the meeting   lobby.
        Returns: Optional[lobby_bypass_settings.LobbyBypassSettings]
        """
        return self._lobby_bypass_settings
    
    @lobby_bypass_settings.setter
    def lobby_bypass_settings(self,value: Optional[lobby_bypass_settings.LobbyBypassSettings] = None) -> None:
        """
        Sets the lobbyBypassSettings property value. Specifies which participants can bypass the meeting   lobby.
        Args:
            value: Value to set for the lobbyBypassSettings property.
        """
        self._lobby_bypass_settings = value
    
    @property
    def participants(self,) -> Optional[meeting_participants.MeetingParticipants]:
        """
        Gets the participants property value. The participants associated with the online meeting.  This includes the organizer and the attendees.
        Returns: Optional[meeting_participants.MeetingParticipants]
        """
        return self._participants
    
    @participants.setter
    def participants(self,value: Optional[meeting_participants.MeetingParticipants] = None) -> None:
        """
        Sets the participants property value. The participants associated with the online meeting.  This includes the organizer and the attendees.
        Args:
            value: Value to set for the participants property.
        """
        self._participants = value
    
    @property
    def record_automatically(self,) -> Optional[bool]:
        """
        Gets the recordAutomatically property value. Indicates whether to record the meeting automatically.
        Returns: Optional[bool]
        """
        return self._record_automatically
    
    @record_automatically.setter
    def record_automatically(self,value: Optional[bool] = None) -> None:
        """
        Sets the recordAutomatically property value. Indicates whether to record the meeting automatically.
        Args:
            value: Value to set for the recordAutomatically property.
        """
        self._record_automatically = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowAttendeeToEnableCamera", self.allow_attendee_to_enable_camera)
        writer.write_bool_value("allowAttendeeToEnableMic", self.allow_attendee_to_enable_mic)
        writer.write_enum_value("allowedPresenters", self.allowed_presenters)
        writer.write_enum_value("allowMeetingChat", self.allow_meeting_chat)
        writer.write_bool_value("allowTeamworkReactions", self.allow_teamwork_reactions)
        writer.write_collection_of_object_values("attendanceReports", self.attendance_reports)
        writer.write_object_value("attendeeReport", self.attendee_report)
        writer.write_object_value("audioConferencing", self.audio_conferencing)
        writer.write_object_value("broadcastSettings", self.broadcast_settings)
        writer.write_object_value("chatInfo", self.chat_info)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_bool_value("isBroadcast", self.is_broadcast)
        writer.write_bool_value("isEntryExitAnnounced", self.is_entry_exit_announced)
        writer.write_object_value("joinInformation", self.join_information)
        writer.write_str_value("joinWebUrl", self.join_web_url)
        writer.write_object_value("lobbyBypassSettings", self.lobby_bypass_settings)
        writer.write_object_value("participants", self.participants)
        writer.write_bool_value("recordAutomatically", self.record_automatically)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("videoTeleconferenceId", self.video_teleconference_id)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The meeting start time in UTC.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The meeting start time in UTC.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject of the online meeting.
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject of the online meeting.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def video_teleconference_id(self,) -> Optional[str]:
        """
        Gets the videoTeleconferenceId property value. The video teleconferencing ID. Read-only.
        Returns: Optional[str]
        """
        return self._video_teleconference_id
    
    @video_teleconference_id.setter
    def video_teleconference_id(self,value: Optional[str] = None) -> None:
        """
        Sets the videoTeleconferenceId property value. The video teleconferencing ID. Read-only.
        Args:
            value: Value to set for the videoTeleconferenceId property.
        """
        self._video_teleconference_id = value
    

