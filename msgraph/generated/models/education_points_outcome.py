from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_assignment_points_grade import EducationAssignmentPointsGrade
    from .education_outcome import EducationOutcome

from .education_outcome import EducationOutcome

@dataclass
class EducationPointsOutcome(EducationOutcome, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationPointsOutcome"
    # The numeric grade the teacher has given the student for this assignment.
    points: Optional[EducationAssignmentPointsGrade] = None
    # A copy of the points property that is made when the grade is released to the student.
    published_points: Optional[EducationAssignmentPointsGrade] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationPointsOutcome:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationPointsOutcome
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationPointsOutcome()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_assignment_points_grade import EducationAssignmentPointsGrade
        from .education_outcome import EducationOutcome

        from .education_assignment_points_grade import EducationAssignmentPointsGrade
        from .education_outcome import EducationOutcome

        fields: dict[str, Callable[[Any], None]] = {
            "points": lambda n : setattr(self, 'points', n.get_object_value(EducationAssignmentPointsGrade)),
            "publishedPoints": lambda n : setattr(self, 'published_points', n.get_object_value(EducationAssignmentPointsGrade)),
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
        writer.write_object_value("points", self.points)
        writer.write_object_value("publishedPoints", self.published_points)
    

