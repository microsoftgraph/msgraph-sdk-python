from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_assignment_grade_type, education_item_body, entity, identity_set, rubric_level, rubric_quality

from . import entity

@dataclass
class EducationRubric(entity.Entity):
    # The user who created this resource.
    created_by: Optional[identity_set.IdentitySet] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime] = None
    # The description of this rubric.
    description: Optional[education_item_body.EducationItemBody] = None
    # The name of this rubric.
    display_name: Optional[str] = None
    # The grading type of this rubric -- null for a no-points rubric, or educationAssignmentPointsGradeType for a points rubric.
    grading: Optional[education_assignment_grade_type.EducationAssignmentGradeType] = None
    # The last user to modify the resource.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # Moment in time when the resource was last modified.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime] = None
    # The collection of levels making up this rubric.
    levels: Optional[List[rubric_level.RubricLevel]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of qualities making up this rubric.
    qualities: Optional[List[rubric_quality.RubricQuality]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationRubric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationRubric
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationRubric()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_assignment_grade_type, education_item_body, entity, identity_set, rubric_level, rubric_quality

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_object_value(education_item_body.EducationItemBody)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "grading": lambda n : setattr(self, 'grading', n.get_object_value(education_assignment_grade_type.EducationAssignmentGradeType)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "levels": lambda n : setattr(self, 'levels', n.get_collection_of_object_values(rubric_level.RubricLevel)),
            "qualities": lambda n : setattr(self, 'qualities', n.get_collection_of_object_values(rubric_quality.RubricQuality)),
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
        writer.write_object_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("grading", self.grading)
        writer.write_collection_of_object_values("levels", self.levels)
        writer.write_collection_of_object_values("qualities", self.qualities)
    

