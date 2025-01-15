from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_outcome import EducationOutcome
    from .rubric_quality_feedback_model import RubricQualityFeedbackModel
    from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel

from .education_outcome import EducationOutcome

@dataclass
class EducationRubricOutcome(EducationOutcome, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationRubricOutcome"
    # A copy of the rubricQualityFeedback property that is made when the grade is released to the student.
    published_rubric_quality_feedback: Optional[list[RubricQualityFeedbackModel]] = None
    # A copy of the rubricQualitySelectedLevels property that is made when the grade is released to the student.
    published_rubric_quality_selected_levels: Optional[list[RubricQualitySelectedColumnModel]] = None
    # A collection of specific feedback for each quality of this rubric.
    rubric_quality_feedback: Optional[list[RubricQualityFeedbackModel]] = None
    # The level that the teacher has selected for each quality while grading this assignment.
    rubric_quality_selected_levels: Optional[list[RubricQualitySelectedColumnModel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationRubricOutcome:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationRubricOutcome
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationRubricOutcome()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_outcome import EducationOutcome
        from .rubric_quality_feedback_model import RubricQualityFeedbackModel
        from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel

        from .education_outcome import EducationOutcome
        from .rubric_quality_feedback_model import RubricQualityFeedbackModel
        from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel

        fields: dict[str, Callable[[Any], None]] = {
            "publishedRubricQualityFeedback": lambda n : setattr(self, 'published_rubric_quality_feedback', n.get_collection_of_object_values(RubricQualityFeedbackModel)),
            "publishedRubricQualitySelectedLevels": lambda n : setattr(self, 'published_rubric_quality_selected_levels', n.get_collection_of_object_values(RubricQualitySelectedColumnModel)),
            "rubricQualityFeedback": lambda n : setattr(self, 'rubric_quality_feedback', n.get_collection_of_object_values(RubricQualityFeedbackModel)),
            "rubricQualitySelectedLevels": lambda n : setattr(self, 'rubric_quality_selected_levels', n.get_collection_of_object_values(RubricQualitySelectedColumnModel)),
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
        writer.write_collection_of_object_values("publishedRubricQualityFeedback", self.published_rubric_quality_feedback)
        writer.write_collection_of_object_values("publishedRubricQualitySelectedLevels", self.published_rubric_quality_selected_levels)
        writer.write_collection_of_object_values("rubricQualityFeedback", self.rubric_quality_feedback)
        writer.write_collection_of_object_values("rubricQualitySelectedLevels", self.rubric_quality_selected_levels)
    

