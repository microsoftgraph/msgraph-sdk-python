from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_added_student_action import EducationAddedStudentAction
    from .education_add_to_calendar_options import EducationAddToCalendarOptions
    from .entity import Entity

from .entity import Entity

@dataclass
class EducationAssignmentDefaults(Entity, Parsable):
    # Optional field to control adding assignments to students' and teachers' calendars when the assignment is published. The possible values are: none, studentsAndPublisher, studentsAndTeamOwners, unknownFutureValue, and studentsOnly. Use the Prefer: include-unknown-enum-members request header to get the following members in this evolvable enum: studentsOnly. The default value is none.
    add_to_calendar_action: Optional[EducationAddToCalendarOptions] = None
    # Class-level default behavior for handling students who are added after the assignment is published. The possible values are: none, assignIfOpen.
    added_student_action: Optional[EducationAddedStudentAction] = None
    # Class-level default value for due time field. Default value is 23:59:00.
    due_time: Optional[datetime.time] = None
    # Default Teams channel to which notifications are sent. Default value is null.
    notification_channel_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationAssignmentDefaults:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentDefaults
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationAssignmentDefaults()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_added_student_action import EducationAddedStudentAction
        from .education_add_to_calendar_options import EducationAddToCalendarOptions
        from .entity import Entity

        from .education_added_student_action import EducationAddedStudentAction
        from .education_add_to_calendar_options import EducationAddToCalendarOptions
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "addToCalendarAction": lambda n : setattr(self, 'add_to_calendar_action', n.get_enum_value(EducationAddToCalendarOptions)),
            "addedStudentAction": lambda n : setattr(self, 'added_student_action', n.get_enum_value(EducationAddedStudentAction)),
            "dueTime": lambda n : setattr(self, 'due_time', n.get_time_value()),
            "notificationChannelUrl": lambda n : setattr(self, 'notification_channel_url', n.get_str_value()),
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
        writer.write_enum_value("addToCalendarAction", self.add_to_calendar_action)
        writer.write_enum_value("addedStudentAction", self.added_student_action)
        writer.write_time_value("dueTime", self.due_time)
        writer.write_str_value("notificationChannelUrl", self.notification_channel_url)
    

