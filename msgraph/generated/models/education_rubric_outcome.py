from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_outcome, rubric_quality_feedback_model, rubric_quality_selected_column_model

from . import education_outcome

@dataclass
class EducationRubricOutcome(education_outcome.EducationOutcome):
    odata_type = "#microsoft.graph.educationRubricOutcome"
    # A copy of the rubricQualityFeedback property that is made when the grade is released to the student.
    published_rubric_quality_feedback: Optional[List[rubric_quality_feedback_model.RubricQualityFeedbackModel]] = None
    # A copy of the rubricQualitySelectedLevels property that is made when the grade is released to the student.
    published_rubric_quality_selected_levels: Optional[List[rubric_quality_selected_column_model.RubricQualitySelectedColumnModel]] = None
    # A collection of specific feedback for each quality of this rubric.
    rubric_quality_feedback: Optional[List[rubric_quality_feedback_model.RubricQualityFeedbackModel]] = None
    # The level that the teacher has selected for each quality while grading this assignment.
    rubric_quality_selected_levels: Optional[List[rubric_quality_selected_column_model.RubricQualitySelectedColumnModel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationRubricOutcome:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationRubricOutcome
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationRubricOutcome()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_outcome, rubric_quality_feedback_model, rubric_quality_selected_column_model

        fields: Dict[str, Callable[[Any], None]] = {
            "publishedRubricQualityFeedback": lambda n : setattr(self, 'published_rubric_quality_feedback', n.get_collection_of_object_values(rubric_quality_feedback_model.RubricQualityFeedbackModel)),
            "publishedRubricQualitySelectedLevels": lambda n : setattr(self, 'published_rubric_quality_selected_levels', n.get_collection_of_object_values(rubric_quality_selected_column_model.RubricQualitySelectedColumnModel)),
            "rubricQualityFeedback": lambda n : setattr(self, 'rubric_quality_feedback', n.get_collection_of_object_values(rubric_quality_feedback_model.RubricQualityFeedbackModel)),
            "rubricQualitySelectedLevels": lambda n : setattr(self, 'rubric_quality_selected_levels', n.get_collection_of_object_values(rubric_quality_selected_column_model.RubricQualitySelectedColumnModel)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("publishedRubricQualityFeedback", self.published_rubric_quality_feedback)
        writer.write_collection_of_object_values("publishedRubricQualitySelectedLevels", self.published_rubric_quality_selected_levels)
        writer.write_collection_of_object_values("rubricQualityFeedback", self.rubric_quality_feedback)
        writer.write_collection_of_object_values("rubricQualitySelectedLevels", self.rubric_quality_selected_levels)
    

