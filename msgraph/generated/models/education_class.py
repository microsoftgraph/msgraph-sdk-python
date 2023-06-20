from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_assignment, education_assignment_defaults, education_assignment_settings, education_category, education_course, education_external_source, education_school, education_term, education_user, entity, group, identity_set

from . import entity

@dataclass
class EducationClass(entity.Entity):
    # All categories associated with this class. Nullable.
    assignment_categories: Optional[List[education_category.EducationCategory]] = None
    # Specifies class-level defaults respected by new assignments created in the class.
    assignment_defaults: Optional[education_assignment_defaults.EducationAssignmentDefaults] = None
    # Specifies class-level assignments settings.
    assignment_settings: Optional[education_assignment_settings.EducationAssignmentSettings] = None
    # All assignments associated with this class. Nullable.
    assignments: Optional[List[education_assignment.EducationAssignment]] = None
    # Class code used by the school to identify the class.
    class_code: Optional[str] = None
    # The course property
    course: Optional[education_course.EducationCourse] = None
    # Entity who created the class
    created_by: Optional[identity_set.IdentitySet] = None
    # Description of the class.
    description: Optional[str] = None
    # Name of the class.
    display_name: Optional[str] = None
    # ID of the class from the syncing system.
    external_id: Optional[str] = None
    # Name of the class in the syncing system.
    external_name: Optional[str] = None
    # How this class was created. Possible values are: sis, manual.
    external_source: Optional[education_external_source.EducationExternalSource] = None
    # The name of the external source this resources was generated from.
    external_source_detail: Optional[str] = None
    # Grade level of the class.
    grade: Optional[str] = None
    # The underlying Microsoft 365 group object.
    group: Optional[group.Group] = None
    # Mail name for sending email to all members, if this is enabled.
    mail_nickname: Optional[str] = None
    # All users in the class. Nullable.
    members: Optional[List[education_user.EducationUser]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # All schools that this class is associated with. Nullable.
    schools: Optional[List[education_school.EducationSchool]] = None
    # All teachers in the class. Nullable.
    teachers: Optional[List[education_user.EducationUser]] = None
    # Term for this class.
    term: Optional[education_term.EducationTerm] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationClass:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationClass
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationClass()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_assignment, education_assignment_defaults, education_assignment_settings, education_category, education_course, education_external_source, education_school, education_term, education_user, entity, group, identity_set

        from . import education_assignment, education_assignment_defaults, education_assignment_settings, education_category, education_course, education_external_source, education_school, education_term, education_user, entity, group, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentCategories": lambda n : setattr(self, 'assignment_categories', n.get_collection_of_object_values(education_category.EducationCategory)),
            "assignmentDefaults": lambda n : setattr(self, 'assignment_defaults', n.get_object_value(education_assignment_defaults.EducationAssignmentDefaults)),
            "assignmentSettings": lambda n : setattr(self, 'assignment_settings', n.get_object_value(education_assignment_settings.EducationAssignmentSettings)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(education_assignment.EducationAssignment)),
            "classCode": lambda n : setattr(self, 'class_code', n.get_str_value()),
            "course": lambda n : setattr(self, 'course', n.get_object_value(education_course.EducationCourse)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "externalName": lambda n : setattr(self, 'external_name', n.get_str_value()),
            "externalSource": lambda n : setattr(self, 'external_source', n.get_enum_value(education_external_source.EducationExternalSource)),
            "externalSourceDetail": lambda n : setattr(self, 'external_source_detail', n.get_str_value()),
            "grade": lambda n : setattr(self, 'grade', n.get_str_value()),
            "group": lambda n : setattr(self, 'group', n.get_object_value(group.Group)),
            "mailNickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(education_user.EducationUser)),
            "schools": lambda n : setattr(self, 'schools', n.get_collection_of_object_values(education_school.EducationSchool)),
            "teachers": lambda n : setattr(self, 'teachers', n.get_collection_of_object_values(education_user.EducationUser)),
            "term": lambda n : setattr(self, 'term', n.get_object_value(education_term.EducationTerm)),
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
        writer.write_collection_of_object_values("assignmentCategories", self.assignment_categories)
        writer.write_object_value("assignmentDefaults", self.assignment_defaults)
        writer.write_object_value("assignmentSettings", self.assignment_settings)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("classCode", self.class_code)
        writer.write_object_value("course", self.course)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("externalName", self.external_name)
        writer.write_enum_value("externalSource", self.external_source)
        writer.write_str_value("externalSourceDetail", self.external_source_detail)
        writer.write_str_value("grade", self.grade)
        writer.write_object_value("group", self.group)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_collection_of_object_values("schools", self.schools)
        writer.write_collection_of_object_values("teachers", self.teachers)
        writer.write_object_value("term", self.term)
    

