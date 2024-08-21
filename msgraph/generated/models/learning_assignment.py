from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assignment_type import AssignmentType
    from .date_time_time_zone import DateTimeTimeZone
    from .item_body import ItemBody
    from .learning_course_activity import LearningCourseActivity

from .learning_course_activity import LearningCourseActivity

@dataclass
class LearningAssignment(LearningCourseActivity):
    # Assigned date for the course activity. Optional.
    assigned_date_time: Optional[datetime.datetime] = None
    # The user ID of the assigner. Optional.
    assigner_user_id: Optional[str] = None
    # The assignmentType property
    assignment_type: Optional[AssignmentType] = None
    # Due date for the course activity. Optional.
    due_date_time: Optional[DateTimeTimeZone] = None
    # Notes for the course activity. Optional.
    notes: Optional[ItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LearningAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LearningAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LearningAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .assignment_type import AssignmentType
        from .date_time_time_zone import DateTimeTimeZone
        from .item_body import ItemBody
        from .learning_course_activity import LearningCourseActivity

        from .assignment_type import AssignmentType
        from .date_time_time_zone import DateTimeTimeZone
        from .item_body import ItemBody
        from .learning_course_activity import LearningCourseActivity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedDateTime": lambda n : setattr(self, 'assigned_date_time', n.get_datetime_value()),
            "assignerUserId": lambda n : setattr(self, 'assigner_user_id', n.get_str_value()),
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_enum_value(AssignmentType)),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_object_value(DateTimeTimeZone)),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(ItemBody)),
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
        writer.write_datetime_value("assignedDateTime", self.assigned_date_time)
        writer.write_str_value("assignerUserId", self.assigner_user_id)
        writer.write_enum_value("assignmentType", self.assignment_type)
        writer.write_object_value("dueDateTime", self.due_date_time)
        writer.write_object_value("notes", self.notes)
    

