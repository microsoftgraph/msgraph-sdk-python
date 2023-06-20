from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_assignment_points_grade, education_outcome

from . import education_outcome

@dataclass
class EducationPointsOutcome(education_outcome.EducationOutcome):
    odata_type = "#microsoft.graph.educationPointsOutcome"
    # The numeric grade the teacher has given the student for this assignment.
    points: Optional[education_assignment_points_grade.EducationAssignmentPointsGrade] = None
    # A copy of the points property that is made when the grade is released to the student.
    published_points: Optional[education_assignment_points_grade.EducationAssignmentPointsGrade] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationPointsOutcome:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationPointsOutcome
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationPointsOutcome()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_assignment_points_grade, education_outcome

        from . import education_assignment_points_grade, education_outcome

        fields: Dict[str, Callable[[Any], None]] = {
            "points": lambda n : setattr(self, 'points', n.get_object_value(education_assignment_points_grade.EducationAssignmentPointsGrade)),
            "publishedPoints": lambda n : setattr(self, 'published_points', n.get_object_value(education_assignment_points_grade.EducationAssignmentPointsGrade)),
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
        writer.write_object_value("points", self.points)
        writer.write_object_value("publishedPoints", self.published_points)
    

