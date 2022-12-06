from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_assignment_grade_type = lazy_import('msgraph.generated.models.education_assignment_grade_type')
education_item_body = lazy_import('msgraph.generated.models.education_item_body')
entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
rubric_level = lazy_import('msgraph.generated.models.rubric_level')
rubric_quality = lazy_import('msgraph.generated.models.rubric_quality')

class EducationRubric(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new educationRubric and sets the default values.
        """
        super().__init__()
        # The user who created this resource.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._created_date_time: Optional[datetime] = None
        # The description of this rubric.
        self._description: Optional[education_item_body.EducationItemBody] = None
        # The name of this rubric.
        self._display_name: Optional[str] = None
        # The grading type of this rubric -- null for a no-points rubric, or educationAssignmentPointsGradeType for a points rubric.
        self._grading: Optional[education_assignment_grade_type.EducationAssignmentGradeType] = None
        # The last user to modify the resource.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # Moment in time when the resource was last modified.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._last_modified_date_time: Optional[datetime] = None
        # The collection of levels making up this rubric.
        self._levels: Optional[List[rubric_level.RubricLevel]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The collection of qualities making up this rubric.
        self._qualities: Optional[List[rubric_quality.RubricQuality]] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The user who created this resource.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The user who created this resource.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
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
    
    @property
    def description(self,) -> Optional[education_item_body.EducationItemBody]:
        """
        Gets the description property value. The description of this rubric.
        Returns: Optional[education_item_body.EducationItemBody]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[education_item_body.EducationItemBody] = None) -> None:
        """
        Sets the description property value. The description of this rubric.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of this rubric.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of this rubric.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_object_value(education_item_body.EducationItemBody)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "grading": lambda n : setattr(self, 'grading', n.get_object_value(education_assignment_grade_type.EducationAssignmentGradeType)),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "levels": lambda n : setattr(self, 'levels', n.get_collection_of_object_values(rubric_level.RubricLevel)),
            "qualities": lambda n : setattr(self, 'qualities', n.get_collection_of_object_values(rubric_quality.RubricQuality)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def grading(self,) -> Optional[education_assignment_grade_type.EducationAssignmentGradeType]:
        """
        Gets the grading property value. The grading type of this rubric -- null for a no-points rubric, or educationAssignmentPointsGradeType for a points rubric.
        Returns: Optional[education_assignment_grade_type.EducationAssignmentGradeType]
        """
        return self._grading
    
    @grading.setter
    def grading(self,value: Optional[education_assignment_grade_type.EducationAssignmentGradeType] = None) -> None:
        """
        Sets the grading property value. The grading type of this rubric -- null for a no-points rubric, or educationAssignmentPointsGradeType for a points rubric.
        Args:
            value: Value to set for the grading property.
        """
        self._grading = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. The last user to modify the resource.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. The last user to modify the resource.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Moment in time when the resource was last modified.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Moment in time when the resource was last modified.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def levels(self,) -> Optional[List[rubric_level.RubricLevel]]:
        """
        Gets the levels property value. The collection of levels making up this rubric.
        Returns: Optional[List[rubric_level.RubricLevel]]
        """
        return self._levels
    
    @levels.setter
    def levels(self,value: Optional[List[rubric_level.RubricLevel]] = None) -> None:
        """
        Sets the levels property value. The collection of levels making up this rubric.
        Args:
            value: Value to set for the levels property.
        """
        self._levels = value
    
    @property
    def qualities(self,) -> Optional[List[rubric_quality.RubricQuality]]:
        """
        Gets the qualities property value. The collection of qualities making up this rubric.
        Returns: Optional[List[rubric_quality.RubricQuality]]
        """
        return self._qualities
    
    @qualities.setter
    def qualities(self,value: Optional[List[rubric_quality.RubricQuality]] = None) -> None:
        """
        Sets the qualities property value. The collection of qualities making up this rubric.
        Args:
            value: Value to set for the qualities property.
        """
        self._qualities = value
    
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
    

