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
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.notebook":
                from . import notebook

                return notebook.Notebook()
            if mapping_value == "#microsoft.graph.onenoteEntityHierarchyModel":
                from . import onenote_entity_hierarchy_model

                return onenote_entity_hierarchy_model.OnenoteEntityHierarchyModel()
            if mapping_value == "#microsoft.graph.onenoteEntitySchemaObjectModel":
                from . import onenote_entity_schema_object_model

                return onenote_entity_schema_object_model.OnenoteEntitySchemaObjectModel()
            if mapping_value == "#microsoft.graph.onenotePage":
                from . import onenote_page

                return onenote_page.OnenotePage()
            if mapping_value == "#microsoft.graph.onenoteResource":
                from . import onenote_resource

                return onenote_resource.OnenoteResource()
            if mapping_value == "#microsoft.graph.onenoteSection":
                from . import onenote_section

                return onenote_section.OnenoteSection()
            if mapping_value == "#microsoft.graph.sectionGroup":
                from . import section_group

                return section_group.SectionGroup()
        return OnenoteEntityBaseModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("self", self.self)
    

