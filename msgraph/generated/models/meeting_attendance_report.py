from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attendance_record import AttendanceRecord
    from .entity import Entity
    from .virtual_event_external_information import VirtualEventExternalInformation

from .entity import Entity

@dataclass
class MeetingAttendanceReport(Entity, Parsable):
    # List of attendance records of an attendance report. Read-only.
    attendance_records: Optional[list[AttendanceRecord]] = None
    # The external information of a virtual event. Returned only for event organizers or coorganizers. Read-only.
    external_event_information: Optional[list[VirtualEventExternalInformation]] = None
    # UTC time when the meeting ended. Read-only.
    meeting_end_date_time: Optional[datetime.datetime] = None
    # UTC time when the meeting started. Read-only.
    meeting_start_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Total number of participants. Read-only.
    total_participant_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingAttendanceReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingAttendanceReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MeetingAttendanceReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attendance_record import AttendanceRecord
        from .entity import Entity
        from .virtual_event_external_information import VirtualEventExternalInformation

        from .attendance_record import AttendanceRecord
        from .entity import Entity
        from .virtual_event_external_information import VirtualEventExternalInformation

        fields: dict[str, Callable[[Any], None]] = {
            "attendanceRecords": lambda n : setattr(self, 'attendance_records', n.get_collection_of_object_values(AttendanceRecord)),
            "externalEventInformation": lambda n : setattr(self, 'external_event_information', n.get_collection_of_object_values(VirtualEventExternalInformation)),
            "meetingEndDateTime": lambda n : setattr(self, 'meeting_end_date_time', n.get_datetime_value()),
            "meetingStartDateTime": lambda n : setattr(self, 'meeting_start_date_time', n.get_datetime_value()),
            "totalParticipantCount": lambda n : setattr(self, 'total_participant_count', n.get_int_value()),
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
        writer.write_collection_of_object_values("attendanceRecords", self.attendance_records)
        writer.write_collection_of_object_values("externalEventInformation", self.external_event_information)
        writer.write_datetime_value("meetingEndDateTime", self.meeting_end_date_time)
        writer.write_datetime_value("meetingStartDateTime", self.meeting_start_date_time)
        writer.write_int_value("totalParticipantCount", self.total_participant_count)
    

