from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .learning_course_activity import LearningCourseActivity

from .learning_course_activity import LearningCourseActivity

@dataclass
class LearningSelfInitiatedCourse(LearningCourseActivity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time on which the learner started the self-initiated course. Optional.
    started_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LearningSelfInitiatedCourse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LearningSelfInitiatedCourse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LearningSelfInitiatedCourse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .learning_course_activity import LearningCourseActivity

        from .learning_course_activity import LearningCourseActivity

        fields: dict[str, Callable[[Any], None]] = {
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("startedDateTime", self.started_date_time)
    

