from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_grading_scheme_grade import EducationGradingSchemeGrade
    from .entity import Entity

from .entity import Entity

@dataclass
class EducationGradingScheme(Entity, Parsable):
    # The name of the grading scheme.
    display_name: Optional[str] = None
    # The grades that make up the scheme.
    grades: Optional[list[EducationGradingSchemeGrade]] = None
    # The display setting for the UI. Indicates whether teachers can grade with points in addition to letter grades.
    hide_points_during_grading: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationGradingScheme:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationGradingScheme
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationGradingScheme()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_grading_scheme_grade import EducationGradingSchemeGrade
        from .entity import Entity

        from .education_grading_scheme_grade import EducationGradingSchemeGrade
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "grades": lambda n : setattr(self, 'grades', n.get_collection_of_object_values(EducationGradingSchemeGrade)),
            "hidePointsDuringGrading": lambda n : setattr(self, 'hide_points_during_grading', n.get_bool_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("grades", self.grades)
        writer.write_bool_value("hidePointsDuringGrading", self.hide_points_during_grading)
    

