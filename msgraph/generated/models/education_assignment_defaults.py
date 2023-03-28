from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_added_student_action, education_add_to_calendar_options, entity

from . import entity

class EducationAssignmentDefaults(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationAssignmentDefaults and sets the default values.
        """
        super().__init__()
        # Optional field to control adding assignments to students' and teachers' calendars when the assignment is published. The possible values are: none, studentsAndPublisher, studentsAndTeamOwners, unknownFutureValue, and studentsOnly. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: studentsOnly. The default value is none.
        self._add_to_calendar_action: Optional[education_add_to_calendar_options.EducationAddToCalendarOptions] = None
        # Class-level default behavior for handling students who are added after the assignment is published. Possible values are: none, assignIfOpen.
        self._added_student_action: Optional[education_added_student_action.EducationAddedStudentAction] = None
        # Class-level default value for due time field. Default value is 23:59:00.
        self._due_time: Optional[time] = None
        # Default Teams channel to which notifications will be sent. Default value is null.
        self._notification_channel_url: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def add_to_calendar_action(self,) -> Optional[education_add_to_calendar_options.EducationAddToCalendarOptions]:
        """
        Gets the addToCalendarAction property value. Optional field to control adding assignments to students' and teachers' calendars when the assignment is published. The possible values are: none, studentsAndPublisher, studentsAndTeamOwners, unknownFutureValue, and studentsOnly. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: studentsOnly. The default value is none.
        Returns: Optional[education_add_to_calendar_options.EducationAddToCalendarOptions]
        """
        return self._add_to_calendar_action
    
    @add_to_calendar_action.setter
    def add_to_calendar_action(self,value: Optional[education_add_to_calendar_options.EducationAddToCalendarOptions] = None) -> None:
        """
        Sets the addToCalendarAction property value. Optional field to control adding assignments to students' and teachers' calendars when the assignment is published. The possible values are: none, studentsAndPublisher, studentsAndTeamOwners, unknownFutureValue, and studentsOnly. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: studentsOnly. The default value is none.
        Args:
            value: Value to set for the add_to_calendar_action property.
        """
        self._add_to_calendar_action = value
    
    @property
    def added_student_action(self,) -> Optional[education_added_student_action.EducationAddedStudentAction]:
        """
        Gets the addedStudentAction property value. Class-level default behavior for handling students who are added after the assignment is published. Possible values are: none, assignIfOpen.
        Returns: Optional[education_added_student_action.EducationAddedStudentAction]
        """
        return self._added_student_action
    
    @added_student_action.setter
    def added_student_action(self,value: Optional[education_added_student_action.EducationAddedStudentAction] = None) -> None:
        """
        Sets the addedStudentAction property value. Class-level default behavior for handling students who are added after the assignment is published. Possible values are: none, assignIfOpen.
        Args:
            value: Value to set for the added_student_action property.
        """
        self._added_student_action = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationAssignmentDefaults:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentDefaults
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationAssignmentDefaults()
    
    @property
    def due_time(self,) -> Optional[time]:
        """
        Gets the dueTime property value. Class-level default value for due time field. Default value is 23:59:00.
        Returns: Optional[time]
        """
        return self._due_time
    
    @due_time.setter
    def due_time(self,value: Optional[time] = None) -> None:
        """
        Sets the dueTime property value. Class-level default value for due time field. Default value is 23:59:00.
        Args:
            value: Value to set for the due_time property.
        """
        self._due_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_added_student_action, education_add_to_calendar_options, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "addedStudentAction": lambda n : setattr(self, 'added_student_action', n.get_enum_value(education_added_student_action.EducationAddedStudentAction)),
            "addToCalendarAction": lambda n : setattr(self, 'add_to_calendar_action', n.get_enum_value(education_add_to_calendar_options.EducationAddToCalendarOptions)),
            "dueTime": lambda n : setattr(self, 'due_time', n.get_time_value()),
            "notificationChannelUrl": lambda n : setattr(self, 'notification_channel_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def notification_channel_url(self,) -> Optional[str]:
        """
        Gets the notificationChannelUrl property value. Default Teams channel to which notifications will be sent. Default value is null.
        Returns: Optional[str]
        """
        return self._notification_channel_url
    
    @notification_channel_url.setter
    def notification_channel_url(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationChannelUrl property value. Default Teams channel to which notifications will be sent. Default value is null.
        Args:
            value: Value to set for the notification_channel_url property.
        """
        self._notification_channel_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("addedStudentAction", self.added_student_action)
        writer.write_enum_value("addToCalendarAction", self.add_to_calendar_action)
        writer.write_time_value("dueTime", self.due_time)
        writer.write_str_value("notificationChannelUrl", self.notification_channel_url)
    

