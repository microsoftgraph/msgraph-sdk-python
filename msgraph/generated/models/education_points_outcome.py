from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_assignment_points_grade = lazy_import('msgraph.generated.models.education_assignment_points_grade')
education_outcome = lazy_import('msgraph.generated.models.education_outcome')

class EducationPointsOutcome(education_outcome.EducationOutcome):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationPointsOutcome and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationPointsOutcome"
        # The numeric grade the teacher has given the student for this assignment.
        self._points: Optional[education_assignment_points_grade.EducationAssignmentPointsGrade] = None
        # A copy of the points property that is made when the grade is released to the student.
        self._published_points: Optional[education_assignment_points_grade.EducationAssignmentPointsGrade] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationPointsOutcome:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationPointsOutcome
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationPointsOutcome()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "points": lambda n : setattr(self, 'points', n.get_object_value(education_assignment_points_grade.EducationAssignmentPointsGrade)),
            "published_points": lambda n : setattr(self, 'published_points', n.get_object_value(education_assignment_points_grade.EducationAssignmentPointsGrade)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def points(self,) -> Optional[education_assignment_points_grade.EducationAssignmentPointsGrade]:
        """
        Gets the points property value. The numeric grade the teacher has given the student for this assignment.
        Returns: Optional[education_assignment_points_grade.EducationAssignmentPointsGrade]
        """
        return self._points
    
    @points.setter
    def points(self,value: Optional[education_assignment_points_grade.EducationAssignmentPointsGrade] = None) -> None:
        """
        Sets the points property value. The numeric grade the teacher has given the student for this assignment.
        Args:
            value: Value to set for the points property.
        """
        self._points = value
    
    @property
    def published_points(self,) -> Optional[education_assignment_points_grade.EducationAssignmentPointsGrade]:
        """
        Gets the publishedPoints property value. A copy of the points property that is made when the grade is released to the student.
        Returns: Optional[education_assignment_points_grade.EducationAssignmentPointsGrade]
        """
        return self._published_points
    
    @published_points.setter
    def published_points(self,value: Optional[education_assignment_points_grade.EducationAssignmentPointsGrade] = None) -> None:
        """
        Sets the publishedPoints property value. A copy of the points property that is made when the grade is released to the student.
        Args:
            value: Value to set for the publishedPoints property.
        """
        self._published_points = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("points", self.points)
        writer.write_object_value("publishedPoints", self.published_points)
    

