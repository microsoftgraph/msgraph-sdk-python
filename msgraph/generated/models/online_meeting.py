from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .broadcast_meeting_settings import BroadcastMeetingSettings
    from .call_recording import CallRecording
    from .call_transcript import CallTranscript
    from .meeting_participants import MeetingParticipants
    from .online_meeting_base import OnlineMeetingBase

from .online_meeting_base import OnlineMeetingBase

@dataclass
class OnlineMeeting(OnlineMeetingBase, Parsable):
    """
    Represents a Microsoft online meeting.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onlineMeeting"
    # The content stream of the attendee report of a Microsoft Teams live event. Read-only.
    attendee_report: Optional[bytes] = None
    # Settings related to a live event.
    broadcast_settings: Optional[BroadcastMeetingSettings] = None
    # The meeting creation time in UTC. Read-only.
    creation_date_time: Optional[datetime.datetime] = None
    # The meeting end time in UTC. Required when you create an online meeting.
    end_date_time: Optional[datetime.datetime] = None
    # The external ID that is a custom identifier. Optional.
    external_id: Optional[str] = None
    # Indicates whether this meeting is a Teams live event.
    is_broadcast: Optional[bool] = None
    # The ID of the meeting template.
    meeting_template_id: Optional[str] = None
    # The participants associated with the online meeting, including the organizer and the attendees.
    participants: Optional[MeetingParticipants] = None
    # The recordings of an online meeting. Read-only.
    recordings: Optional[list[CallRecording]] = None
    # The meeting start time in UTC.
    start_date_time: Optional[datetime.datetime] = None
    # The transcripts of an online meeting. Read-only.
    transcripts: Optional[list[CallTranscript]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnlineMeeting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeeting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnlineMeeting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .broadcast_meeting_settings import BroadcastMeetingSettings
        from .call_recording import CallRecording
        from .call_transcript import CallTranscript
        from .meeting_participants import MeetingParticipants
        from .online_meeting_base import OnlineMeetingBase

        from .broadcast_meeting_settings import BroadcastMeetingSettings
        from .call_recording import CallRecording
        from .call_transcript import CallTranscript
        from .meeting_participants import MeetingParticipants
        from .online_meeting_base import OnlineMeetingBase

        fields: dict[str, Callable[[Any], None]] = {
            "attendeeReport": lambda n : setattr(self, 'attendee_report', n.get_bytes_value()),
            "broadcastSettings": lambda n : setattr(self, 'broadcast_settings', n.get_object_value(BroadcastMeetingSettings)),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "isBroadcast": lambda n : setattr(self, 'is_broadcast', n.get_bool_value()),
            "meetingTemplateId": lambda n : setattr(self, 'meeting_template_id', n.get_str_value()),
            "participants": lambda n : setattr(self, 'participants', n.get_object_value(MeetingParticipants)),
            "recordings": lambda n : setattr(self, 'recordings', n.get_collection_of_object_values(CallRecording)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "transcripts": lambda n : setattr(self, 'transcripts', n.get_collection_of_object_values(CallTranscript)),
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
        writer.write_bytes_value("attendeeReport", self.attendee_report)
        writer.write_object_value("broadcastSettings", self.broadcast_settings)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_bool_value("isBroadcast", self.is_broadcast)
        writer.write_str_value("meetingTemplateId", self.meeting_template_id)
        writer.write_object_value("participants", self.participants)
        writer.write_collection_of_object_values("recordings", self.recordings)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_collection_of_object_values("transcripts", self.transcripts)
    

