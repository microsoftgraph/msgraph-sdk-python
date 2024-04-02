from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .authority_template import AuthorityTemplate
    from .category_template import CategoryTemplate
    from .citation_template import CitationTemplate
    from .department_template import DepartmentTemplate
    from .file_plan_applied_category import FilePlanAppliedCategory
    from .file_plan_authority import FilePlanAuthority
    from .file_plan_citation import FilePlanCitation
    from .file_plan_department import FilePlanDepartment
    from .file_plan_reference import FilePlanReference
    from .file_plan_reference_template import FilePlanReferenceTemplate

from ..entity import Entity

@dataclass
class FilePlanDescriptor(Entity):
    # The authority property
    authority: Optional[FilePlanAuthority] = None
    # The authorityTemplate property
    authority_template: Optional[AuthorityTemplate] = None
    # The category property
    category: Optional[FilePlanAppliedCategory] = None
    # The categoryTemplate property
    category_template: Optional[CategoryTemplate] = None
    # The citation property
    citation: Optional[FilePlanCitation] = None
    # The citationTemplate property
    citation_template: Optional[CitationTemplate] = None
    # The department property
    department: Optional[FilePlanDepartment] = None
    # The departmentTemplate property
    department_template: Optional[DepartmentTemplate] = None
    # The filePlanReference property
    file_plan_reference: Optional[FilePlanReference] = None
    # The filePlanReferenceTemplate property
    file_plan_reference_template: Optional[FilePlanReferenceTemplate] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilePlanDescriptor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilePlanDescriptor
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FilePlanDescriptor()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .authority_template import AuthorityTemplate
        from .category_template import CategoryTemplate
        from .citation_template import CitationTemplate
        from .department_template import DepartmentTemplate
        from .file_plan_applied_category import FilePlanAppliedCategory
        from .file_plan_authority import FilePlanAuthority
        from .file_plan_citation import FilePlanCitation
        from .file_plan_department import FilePlanDepartment
        from .file_plan_reference import FilePlanReference
        from .file_plan_reference_template import FilePlanReferenceTemplate

        from ..entity import Entity
        from .authority_template import AuthorityTemplate
        from .category_template import CategoryTemplate
        from .citation_template import CitationTemplate
        from .department_template import DepartmentTemplate
        from .file_plan_applied_category import FilePlanAppliedCategory
        from .file_plan_authority import FilePlanAuthority
        from .file_plan_citation import FilePlanCitation
        from .file_plan_department import FilePlanDepartment
        from .file_plan_reference import FilePlanReference
        from .file_plan_reference_template import FilePlanReferenceTemplate

        fields: Dict[str, Callable[[Any], None]] = {
            "authority": lambda n : setattr(self, 'authority', n.get_object_value(FilePlanAuthority)),
            "authorityTemplate": lambda n : setattr(self, 'authority_template', n.get_object_value(AuthorityTemplate)),
            "category": lambda n : setattr(self, 'category', n.get_object_value(FilePlanAppliedCategory)),
            "categoryTemplate": lambda n : setattr(self, 'category_template', n.get_object_value(CategoryTemplate)),
            "citation": lambda n : setattr(self, 'citation', n.get_object_value(FilePlanCitation)),
            "citationTemplate": lambda n : setattr(self, 'citation_template', n.get_object_value(CitationTemplate)),
            "department": lambda n : setattr(self, 'department', n.get_object_value(FilePlanDepartment)),
            "departmentTemplate": lambda n : setattr(self, 'department_template', n.get_object_value(DepartmentTemplate)),
            "filePlanReference": lambda n : setattr(self, 'file_plan_reference', n.get_object_value(FilePlanReference)),
            "filePlanReferenceTemplate": lambda n : setattr(self, 'file_plan_reference_template', n.get_object_value(FilePlanReferenceTemplate)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("authority", self.authority)
        writer.write_object_value("authorityTemplate", self.authority_template)
        writer.write_object_value("category", self.category)
        writer.write_object_value("categoryTemplate", self.category_template)
        writer.write_object_value("citation", self.citation)
        writer.write_object_value("citationTemplate", self.citation_template)
        writer.write_object_value("department", self.department)
        writer.write_object_value("departmentTemplate", self.department_template)
        writer.write_object_value("filePlanReference", self.file_plan_reference)
        writer.write_object_value("filePlanReferenceTemplate", self.file_plan_reference_template)
    

