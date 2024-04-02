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
    from .file_plan_reference_template import FilePlanReferenceTemplate
    from .retention_label import RetentionLabel

from ..entity import Entity

@dataclass
class LabelsRoot(Entity):
    # The authorities property
    authorities: Optional[List[AuthorityTemplate]] = None
    # The categories property
    categories: Optional[List[CategoryTemplate]] = None
    # The citations property
    citations: Optional[List[CitationTemplate]] = None
    # The departments property
    departments: Optional[List[DepartmentTemplate]] = None
    # The filePlanReferences property
    file_plan_references: Optional[List[FilePlanReferenceTemplate]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The retentionLabels property
    retention_labels: Optional[List[RetentionLabel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LabelsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LabelsRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LabelsRoot()
    
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
        from .file_plan_reference_template import FilePlanReferenceTemplate
        from .retention_label import RetentionLabel

        from ..entity import Entity
        from .authority_template import AuthorityTemplate
        from .category_template import CategoryTemplate
        from .citation_template import CitationTemplate
        from .department_template import DepartmentTemplate
        from .file_plan_reference_template import FilePlanReferenceTemplate
        from .retention_label import RetentionLabel

        fields: Dict[str, Callable[[Any], None]] = {
            "authorities": lambda n : setattr(self, 'authorities', n.get_collection_of_object_values(AuthorityTemplate)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(CategoryTemplate)),
            "citations": lambda n : setattr(self, 'citations', n.get_collection_of_object_values(CitationTemplate)),
            "departments": lambda n : setattr(self, 'departments', n.get_collection_of_object_values(DepartmentTemplate)),
            "filePlanReferences": lambda n : setattr(self, 'file_plan_references', n.get_collection_of_object_values(FilePlanReferenceTemplate)),
            "retentionLabels": lambda n : setattr(self, 'retention_labels', n.get_collection_of_object_values(RetentionLabel)),
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
        writer.write_collection_of_object_values("authorities", self.authorities)
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_collection_of_object_values("citations", self.citations)
        writer.write_collection_of_object_values("departments", self.departments)
        writer.write_collection_of_object_values("filePlanReferences", self.file_plan_references)
        writer.write_collection_of_object_values("retentionLabels", self.retention_labels)
    

