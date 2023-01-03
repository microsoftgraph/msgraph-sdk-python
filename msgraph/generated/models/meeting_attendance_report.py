from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attendance_record = lazy_import('msgraph.generated.models.attendance_record')
entity = lazy_import('msgraph.generated.models.entity')

class MeetingAttendanceReport(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def attendance_records(self,) -> Optional[List[attendance_record.AttendanceRecord]]:
        """
        Gets the attendanceRecords property value. List of attendance records of an attendance report. Read-only.
        Returns: Optional[List[attendance_record.AttendanceRecord]]
        """
        return self._attendance_records
    
    @attendance_records.setter
    def attendance_records(self,value: Optional[List[attendance_record.AttendanceRecord]] = None) -> None:
        """
        Sets the attendanceRecords property value. List of attendance records of an attendance report. Read-only.
        Args:
            value: Value to set for the attendanceRecords property.
        """
        self._attendance_records = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new meetingAttendanceReport and sets the default values.
        """
        super().__init__()
        # List of attendance records of an attendance report. Read-only.
        self._attendance_records: Optional[List[attendance_record.AttendanceRecord]] = None
        # UTC time when the meeting ended. Read-only.
        self._meeting_end_date_time: Optional[datetime] = None
        # UTC time when the meeting started. Read-only.
        self._meeting_start_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Total number of participants. Read-only.
        self._total_participant_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingAttendanceReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingAttendanceReport
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingAttendanceReport()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attendance_records": lambda n : setattr(self, 'attendance_records', n.get_collection_of_object_values(attendance_record.AttendanceRecord)),
            "meeting_end_date_time": lambda n : setattr(self, 'meeting_end_date_time', n.get_datetime_value()),
            "meeting_start_date_time": lambda n : setattr(self, 'meeting_start_date_time', n.get_datetime_value()),
            "total_participant_count": lambda n : setattr(self, 'total_participant_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def meeting_end_date_time(self,) -> Optional[datetime]:
        """
        Gets the meetingEndDateTime property value. UTC time when the meeting ended. Read-only.
        Returns: Optional[datetime]
        """
        return self._meeting_end_date_time
    
    @meeting_end_date_time.setter
    def meeting_end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the meetingEndDateTime property value. UTC time when the meeting ended. Read-only.
        Args:
            value: Value to set for the meetingEndDateTime property.
        """
        self._meeting_end_date_time = value
    
    @property
    def meeting_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the meetingStartDateTime property value. UTC time when the meeting started. Read-only.
        Returns: Optional[datetime]
        """
        return self._meeting_start_date_time
    
    @meeting_start_date_time.setter
    def meeting_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the meetingStartDateTime property value. UTC time when the meeting started. Read-only.
        Args:
            value: Value to set for the meetingStartDateTime property.
        """
        self._meeting_start_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("attendanceRecords", self.attendance_records)
        writer.write_datetime_value("meetingEndDateTime", self.meeting_end_date_time)
        writer.write_datetime_value("meetingStartDateTime", self.meeting_start_date_time)
        writer.write_int_value("totalParticipantCount", self.total_participant_count)
    
    @property
    def total_participant_count(self,) -> Optional[int]:
        """
        Gets the totalParticipantCount property value. Total number of participants. Read-only.
        Returns: Optional[int]
        """
        return self._total_participant_count
    
    @total_participant_count.setter
    def total_participant_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalParticipantCount property value. Total number of participants. Read-only.
        Args:
            value: Value to set for the totalParticipantCount property.
        """
        self._total_participant_count = value
    

