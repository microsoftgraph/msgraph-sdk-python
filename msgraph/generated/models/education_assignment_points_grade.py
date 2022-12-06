from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_assignment_grade = lazy_import('msgraph.generated.models.education_assignment_grade')

class EducationAssignmentPointsGrade(education_assignment_grade.EducationAssignmentGrade):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationAssignmentPointsGrade and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationAssignmentPointsGrade"
        # Number of points a teacher is giving this submission object.
        self._points: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationAssignmentPointsGrade:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentPointsGrade
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationAssignmentPointsGrade()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "points": lambda n : setattr(self, 'points', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def points(self,) -> Optional[float]:
        """
        Gets the points property value. Number of points a teacher is giving this submission object.
        Returns: Optional[float]
        """
        return self._points
    
    @points.setter
    def points(self,value: Optional[float] = None) -> None:
        """
        Sets the points property value. Number of points a teacher is giving this submission object.
        Args:
            value: Value to set for the points property.
        """
        self._points = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_float_value("points", self.points)
    

