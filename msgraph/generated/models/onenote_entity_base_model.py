from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, notebook, onenote_entity_hierarchy_model, onenote_entity_schema_object_model, onenote_page, onenote_resource, onenote_section, section_group

from . import entity

@dataclass
class OnenoteEntityBaseModel(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The endpoint where you can get details about the page. Read-only.
    self: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnenoteEntityBaseModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnenoteEntityBaseModel
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.notebook".casefold():
            from . import notebook

            return notebook.Notebook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntityHierarchyModel".casefold():
            from . import onenote_entity_hierarchy_model

            return onenote_entity_hierarchy_model.OnenoteEntityHierarchyModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntitySchemaObjectModel".casefold():
            from . import onenote_entity_schema_object_model

            return onenote_entity_schema_object_model.OnenoteEntitySchemaObjectModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenotePage".casefold():
            from . import onenote_page

            return onenote_page.OnenotePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteResource".casefold():
            from . import onenote_resource

            return onenote_resource.OnenoteResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteSection".casefold():
            from . import onenote_section

            return onenote_section.OnenoteSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sectionGroup".casefold():
            from . import section_group

            return section_group.SectionGroup()
        return OnenoteEntityBaseModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, notebook, onenote_entity_hierarchy_model, onenote_entity_schema_object_model, onenote_page, onenote_resource, onenote_section, section_group

        from . import entity, notebook, onenote_entity_hierarchy_model, onenote_entity_schema_object_model, onenote_page, onenote_resource, onenote_section, section_group

        fields: Dict[str, Callable[[Any], None]] = {
            "self": lambda n : setattr(self, 'self', n.get_str_value()),
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
        writer.write_str_value("self", self.self)
    

