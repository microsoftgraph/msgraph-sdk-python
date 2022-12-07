from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_assignment_grade_type = lazy_import('msgraph.generated.models.education_assignment_grade_type')

class EducationAssignmentPointsGradeType(education_assignment_grade_type.EducationAssignmentGradeType):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationAssignmentPointsGradeType and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationAssignmentPointsGradeType"
        # Max points possible for this assignment.
        self._max_points: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationAssignmentPointsGradeType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentPointsGradeType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationAssignmentPointsGradeType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "max_points": lambda n : setattr(self, 'max_points', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def max_points(self,) -> Optional[float]:
        """
        Gets the maxPoints property value. Max points possible for this assignment.
        Returns: Optional[float]
        """
        return self._max_points
    
    @max_points.setter
    def max_points(self,value: Optional[float] = None) -> None:
        """
        Sets the maxPoints property value. Max points possible for this assignment.
        Args:
            value: Value to set for the maxPoints property.
        """
        self._max_points = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_float_value("maxPoints", self.max_points)
    

