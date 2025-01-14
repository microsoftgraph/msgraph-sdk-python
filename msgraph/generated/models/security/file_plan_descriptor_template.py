from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..identity_set import IdentitySet
    from .authority_template import AuthorityTemplate
    from .category_template import CategoryTemplate
    from .citation_template import CitationTemplate
    from .department_template import DepartmentTemplate
    from .file_plan_reference_template import FilePlanReferenceTemplate
    from .subcategory_template import SubcategoryTemplate

from ..entity import Entity

@dataclass
class FilePlanDescriptorTemplate(Entity, Parsable):
    # Represents the user who created the filePlanDescriptorTemplate column.
    created_by: Optional[IdentitySet] = None
    # Represents the date and time in which the filePlanDescriptorTemplate is created.
    created_date_time: Optional[datetime.datetime] = None
    # Unique string that defines a filePlanDescriptorTemplate name.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilePlanDescriptorTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilePlanDescriptorTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.authorityTemplate".casefold():
            from .authority_template import AuthorityTemplate

            return AuthorityTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.categoryTemplate".casefold():
            from .category_template import CategoryTemplate

            return CategoryTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.citationTemplate".casefold():
            from .citation_template import CitationTemplate

            return CitationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.departmentTemplate".casefold():
            from .department_template import DepartmentTemplate

            return DepartmentTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanReferenceTemplate".casefold():
            from .file_plan_reference_template import FilePlanReferenceTemplate

            return FilePlanReferenceTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.subcategoryTemplate".casefold():
            from .subcategory_template import SubcategoryTemplate

            return SubcategoryTemplate()
        return FilePlanDescriptorTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .authority_template import AuthorityTemplate
        from .category_template import CategoryTemplate
        from .citation_template import CitationTemplate
        from .department_template import DepartmentTemplate
        from .file_plan_reference_template import FilePlanReferenceTemplate
        from .subcategory_template import SubcategoryTemplate

        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .authority_template import AuthorityTemplate
        from .category_template import CategoryTemplate
        from .citation_template import CitationTemplate
        from .department_template import DepartmentTemplate
        from .file_plan_reference_template import FilePlanReferenceTemplate
        from .subcategory_template import SubcategoryTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
    

