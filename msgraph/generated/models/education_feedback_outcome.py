from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_feedback = lazy_import('msgraph.generated.models.education_feedback')
education_outcome = lazy_import('msgraph.generated.models.education_outcome')

class EducationFeedbackOutcome(education_outcome.EducationOutcome):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationFeedbackOutcome and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationFeedbackOutcome"
        # Teacher's written feedback to the student.
        self._feedback: Optional[education_feedback.EducationFeedback] = None
        # A copy of the feedback property that is made when the grade is released to the student.
        self._published_feedback: Optional[education_feedback.EducationFeedback] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationFeedbackOutcome:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationFeedbackOutcome
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationFeedbackOutcome()
    
    @property
    def feedback(self,) -> Optional[education_feedback.EducationFeedback]:
        """
        Gets the feedback property value. Teacher's written feedback to the student.
        Returns: Optional[education_feedback.EducationFeedback]
        """
        return self._feedback
    
    @feedback.setter
    def feedback(self,value: Optional[education_feedback.EducationFeedback] = None) -> None:
        """
        Sets the feedback property value. Teacher's written feedback to the student.
        Args:
            value: Value to set for the feedback property.
        """
        self._feedback = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "feedback": lambda n : setattr(self, 'feedback', n.get_object_value(education_feedback.EducationFeedback)),
            "published_feedback": lambda n : setattr(self, 'published_feedback', n.get_object_value(education_feedback.EducationFeedback)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def published_feedback(self,) -> Optional[education_feedback.EducationFeedback]:
        """
        Gets the publishedFeedback property value. A copy of the feedback property that is made when the grade is released to the student.
        Returns: Optional[education_feedback.EducationFeedback]
        """
        return self._published_feedback
    
    @published_feedback.setter
    def published_feedback(self,value: Optional[education_feedback.EducationFeedback] = None) -> None:
        """
        Sets the publishedFeedback property value. A copy of the feedback property that is made when the grade is released to the student.
        Args:
            value: Value to set for the publishedFeedback property.
        """
        self._published_feedback = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("feedback", self.feedback)
        writer.write_object_value("publishedFeedback", self.published_feedback)
    

