from __future__ import annotations
from dataclasses import dataclass, field
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_added_student_action, education_add_to_calendar_options, entity

from . import entity

@dataclass
class EducationAssignmentDefaults(entity.Entity):
    # Optional field to control adding assignments to students' and teachers' calendars when the assignment is published. The possible values are: none, studentsAndPublisher, studentsAndTeamOwners, unknownFutureValue, and studentsOnly. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: studentsOnly. The default value is none.
    add_to_calendar_action: Optional[education_add_to_calendar_options.EducationAddToCalendarOptions] = None
    # Class-level default behavior for handling students who are added after the assignment is published. Possible values are: none, assignIfOpen.
    added_student_action: Optional[education_added_student_action.EducationAddedStudentAction] = None
    # Class-level default value for due time field. Default value is 23:59:00.
    due_time: Optional[time] = None
    # Default Teams channel to which notifications will be sent. Default value is null.
    notification_channel_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationAssignmentDefaults:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentDefaults
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationAssignmentDefaults()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_added_student_action, education_add_to_calendar_options, entity

        from . import education_added_student_action, education_add_to_calendar_options, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "addToCalendarAction": lambda n : setattr(self, 'add_to_calendar_action', n.get_enum_value(education_add_to_calendar_options.EducationAddToCalendarOptions)),
            "addedStudentAction": lambda n : setattr(self, 'added_student_action', n.get_enum_value(education_added_student_action.EducationAddedStudentAction)),
            "dueTime": lambda n : setattr(self, 'due_time', n.get_time_value()),
            "notificationChannelUrl": lambda n : setattr(self, 'notification_channel_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("addToCalendarAction", self.add_to_calendar_action)
        writer.write_enum_value("addedStudentAction", self.added_student_action)
        writer.write_time_value("dueTime", self.due_time)
        writer.write_str_value("notificationChannelUrl", self.notification_channel_url)
    

