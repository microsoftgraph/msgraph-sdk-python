from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attendance_interval import AttendanceInterval
    from .entity import Entity
    from .identity import Identity
    from .virtual_event_external_registration_information import VirtualEventExternalRegistrationInformation

from .entity import Entity

@dataclass
class AttendanceRecord(Entity, Parsable):
    # List of time periods between joining and leaving a meeting.
    attendance_intervals: Optional[list[AttendanceInterval]] = None
    # Email address of the user associated with this attendance record.
    email_address: Optional[str] = None
    # The external information for a virtualEventRegistration.
    external_registration_information: Optional[VirtualEventExternalRegistrationInformation] = None
    # The identity of the user associated with this attendance record. The specific type is one of the following derived types of identity, depending on the user type: communicationsUserIdentity, azureCommunicationServicesUserIdentity.
    identity: Optional[Identity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier of a virtualEventRegistration that is available to all participants registered for the virtualEventWebinar.
    registration_id: Optional[str] = None
    # Role of the attendee. The possible values are: None, Attendee, Presenter, and Organizer.
    role: Optional[str] = None
    # Total duration of the attendances in seconds.
    total_attendance_in_seconds: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttendanceRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttendanceRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttendanceRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attendance_interval import AttendanceInterval
        from .entity import Entity
        from .identity import Identity
        from .virtual_event_external_registration_information import VirtualEventExternalRegistrationInformation

        from .attendance_interval import AttendanceInterval
        from .entity import Entity
        from .identity import Identity
        from .virtual_event_external_registration_information import VirtualEventExternalRegistrationInformation

        fields: dict[str, Callable[[Any], None]] = {
            "attendanceIntervals": lambda n : setattr(self, 'attendance_intervals', n.get_collection_of_object_values(AttendanceInterval)),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "externalRegistrationInformation": lambda n : setattr(self, 'external_registration_information', n.get_object_value(VirtualEventExternalRegistrationInformation)),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(Identity)),
            "registrationId": lambda n : setattr(self, 'registration_id', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "totalAttendanceInSeconds": lambda n : setattr(self, 'total_attendance_in_seconds', n.get_int_value()),
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
        writer.write_collection_of_object_values("attendanceIntervals", self.attendance_intervals)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_object_value("externalRegistrationInformation", self.external_registration_information)
        writer.write_object_value("identity", self.identity)
        writer.write_str_value("registrationId", self.registration_id)
        writer.write_str_value("role", self.role)
        writer.write_int_value("totalAttendanceInSeconds", self.total_attendance_in_seconds)
    

