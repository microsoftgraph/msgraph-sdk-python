from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_outcome, rubric_quality_feedback_model, rubric_quality_selected_column_model

from . import education_outcome

class EducationRubricOutcome(education_outcome.EducationOutcome):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationRubricOutcome and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationRubricOutcome"
        # A copy of the rubricQualityFeedback property that is made when the grade is released to the student.
        self._published_rubric_quality_feedback: Optional[List[rubric_quality_feedback_model.RubricQualityFeedbackModel]] = None
        # A copy of the rubricQualitySelectedLevels property that is made when the grade is released to the student.
        self._published_rubric_quality_selected_levels: Optional[List[rubric_quality_selected_column_model.RubricQualitySelectedColumnModel]] = None
        # A collection of specific feedback for each quality of this rubric.
        self._rubric_quality_feedback: Optional[List[rubric_quality_feedback_model.RubricQualityFeedbackModel]] = None
        # The level that the teacher has selected for each quality while grading this assignment.
        self._rubric_quality_selected_levels: Optional[List[rubric_quality_selected_column_model.RubricQualitySelectedColumnModel]] = None
    
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
    
    @property
    def published_rubric_quality_feedback(self,) -> Optional[List[rubric_quality_feedback_model.RubricQualityFeedbackModel]]:
        """
        Gets the publishedRubricQualityFeedback property value. A copy of the rubricQualityFeedback property that is made when the grade is released to the student.
        Returns: Optional[List[rubric_quality_feedback_model.RubricQualityFeedbackModel]]
        """
        return self._published_rubric_quality_feedback
    
    @published_rubric_quality_feedback.setter
    def published_rubric_quality_feedback(self,value: Optional[List[rubric_quality_feedback_model.RubricQualityFeedbackModel]] = None) -> None:
        """
        Sets the publishedRubricQualityFeedback property value. A copy of the rubricQualityFeedback property that is made when the grade is released to the student.
        Args:
            value: Value to set for the published_rubric_quality_feedback property.
        """
        self._published_rubric_quality_feedback = value
    
    @property
    def published_rubric_quality_selected_levels(self,) -> Optional[List[rubric_quality_selected_column_model.RubricQualitySelectedColumnModel]]:
        """
        Gets the publishedRubricQualitySelectedLevels property value. A copy of the rubricQualitySelectedLevels property that is made when the grade is released to the student.
        Returns: Optional[List[rubric_quality_selected_column_model.RubricQualitySelectedColumnModel]]
        """
        return self._published_rubric_quality_selected_levels
    
    @published_rubric_quality_selected_levels.setter
    def published_rubric_quality_selected_levels(self,value: Optional[List[rubric_quality_selected_column_model.RubricQualitySelectedColumnModel]] = None) -> None:
        """
        Sets the publishedRubricQualitySelectedLevels property value. A copy of the rubricQualitySelectedLevels property that is made when the grade is released to the student.
        Args:
            value: Value to set for the published_rubric_quality_selected_levels property.
        """
        self._published_rubric_quality_selected_levels = value
    
    @property
    def rubric_quality_feedback(self,) -> Optional[List[rubric_quality_feedback_model.RubricQualityFeedbackModel]]:
        """
        Gets the rubricQualityFeedback property value. A collection of specific feedback for each quality of this rubric.
        Returns: Optional[List[rubric_quality_feedback_model.RubricQualityFeedbackModel]]
        """
        return self._rubric_quality_feedback
    
    @rubric_quality_feedback.setter
    def rubric_quality_feedback(self,value: Optional[List[rubric_quality_feedback_model.RubricQualityFeedbackModel]] = None) -> None:
        """
        Sets the rubricQualityFeedback property value. A collection of specific feedback for each quality of this rubric.
        Args:
            value: Value to set for the rubric_quality_feedback property.
        """
        self._rubric_quality_feedback = value
    
    @property
    def rubric_quality_selected_levels(self,) -> Optional[List[rubric_quality_selected_column_model.RubricQualitySelectedColumnModel]]:
        """
        Gets the rubricQualitySelectedLevels property value. The level that the teacher has selected for each quality while grading this assignment.
        Returns: Optional[List[rubric_quality_selected_column_model.RubricQualitySelectedColumnModel]]
        """
        return self._rubric_quality_selected_levels
    
    @rubric_quality_selected_levels.setter
    def rubric_quality_selected_levels(self,value: Optional[List[rubric_quality_selected_column_model.RubricQualitySelectedColumnModel]] = None) -> None:
        """
        Sets the rubricQualitySelectedLevels property value. The level that the teacher has selected for each quality while grading this assignment.
        Args:
            value: Value to set for the rubric_quality_selected_levels property.
        """
        self._rubric_quality_selected_levels = value
    
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
    

