from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_add_to_calendar_options = lazy_import('msgraph.generated.models.education_add_to_calendar_options')
education_added_student_action = lazy_import('msgraph.generated.models.education_added_student_action')
entity = lazy_import('msgraph.generated.models.entity')

class EducationAssignmentDefaults(entity.Entity):
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
            value: Value to set for the addedStudentAction property.
        """
        self._added_student_action = value
    
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
            value: Value to set for the addToCalendarAction property.
        """
        self._add_to_calendar_action = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new educationAssignmentDefaults and sets the default values.
        """
        super().__init__()
        # Class-level default behavior for handling students who are added after the assignment is published. Possible values are: none, assignIfOpen.
        self._added_student_action: Optional[education_added_student_action.EducationAddedStudentAction] = None
        # Optional field to control adding assignments to students' and teachers' calendars when the assignment is published. The possible values are: none, studentsAndPublisher, studentsAndTeamOwners, unknownFutureValue, and studentsOnly. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: studentsOnly. The default value is none.
        self._add_to_calendar_action: Optional[education_add_to_calendar_options.EducationAddToCalendarOptions] = None
        # Class-level default value for due time field. Default value is 23:59:00.
        self._due_time: Optional[Time] = None
        # Default Teams channel to which notifications will be sent. Default value is null.
        self._notification_channel_url: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
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
    def due_time(self,) -> Optional[Time]:
        """
        Gets the dueTime property value. Class-level default value for due time field. Default value is 23:59:00.
        Returns: Optional[Time]
        """
        return self._due_time
    
    @due_time.setter
    def due_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the dueTime property value. Class-level default value for due time field. Default value is 23:59:00.
        Args:
            value: Value to set for the dueTime property.
        """
        self._due_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "added_student_action": lambda n : setattr(self, 'added_student_action', n.get_enum_value(education_added_student_action.EducationAddedStudentAction)),
            "add_to_calendar_action": lambda n : setattr(self, 'add_to_calendar_action', n.get_enum_value(education_add_to_calendar_options.EducationAddToCalendarOptions)),
            "due_time": lambda n : setattr(self, 'due_time', n.get_object_value(Time)),
            "notification_channel_url": lambda n : setattr(self, 'notification_channel_url', n.get_str_value()),
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
            value: Value to set for the notificationChannelUrl property.
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
        writer.write_object_value("dueTime", self.due_time)
        writer.write_str_value("notificationChannelUrl", self.notification_channel_url)
    

