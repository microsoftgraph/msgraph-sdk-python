from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .course_status import CourseStatus
    from .entity import Entity
    from .learning_assignment import LearningAssignment
    from .learning_self_initiated_course import LearningSelfInitiatedCourse

from .entity import Entity

@dataclass
class LearningCourseActivity(Entity):
    # Date and time when the assignment was completed. Optional.
    completed_date_time: Optional[datetime.datetime] = None
    # The percentage completion value of the course activity. Optional.
    completion_percentage: Optional[int] = None
    # The externalcourseActivityId property
    externalcourse_activity_id: Optional[str] = None
    # The user ID of the learner to whom the activity is assigned. Required.
    learner_user_id: Optional[str] = None
    # The ID of the learning content created in Viva Learning. Required.
    learning_content_id: Optional[str] = None
    # The registration ID of the provider. Required.
    learning_provider_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the course activity. Possible values are: notStarted, inProgress, completed. Required.
    status: Optional[CourseStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LearningCourseActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LearningCourseActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningAssignment".casefold():
            from .learning_assignment import LearningAssignment

            return LearningAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningSelfInitiatedCourse".casefold():
            from .learning_self_initiated_course import LearningSelfInitiatedCourse

            return LearningSelfInitiatedCourse()
        return LearningCourseActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .course_status import CourseStatus
        from .entity import Entity
        from .learning_assignment import LearningAssignment
        from .learning_self_initiated_course import LearningSelfInitiatedCourse

        from .course_status import CourseStatus
        from .entity import Entity
        from .learning_assignment import LearningAssignment
        from .learning_self_initiated_course import LearningSelfInitiatedCourse

        fields: Dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "completionPercentage": lambda n : setattr(self, 'completion_percentage', n.get_int_value()),
            "externalcourseActivityId": lambda n : setattr(self, 'externalcourse_activity_id', n.get_str_value()),
            "learnerUserId": lambda n : setattr(self, 'learner_user_id', n.get_str_value()),
            "learningContentId": lambda n : setattr(self, 'learning_content_id', n.get_str_value()),
            "learningProviderId": lambda n : setattr(self, 'learning_provider_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CourseStatus)),
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
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_int_value("completionPercentage", self.completion_percentage)
        writer.write_str_value("externalcourseActivityId", self.externalcourse_activity_id)
        writer.write_str_value("learnerUserId", self.learner_user_id)
        writer.write_str_value("learningContentId", self.learning_content_id)
        writer.write_str_value("learningProviderId", self.learning_provider_id)
        writer.write_enum_value("status", self.status)
    

