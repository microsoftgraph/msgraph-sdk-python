from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .notebook import Notebook
    from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
    from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
    from .onenote_page import OnenotePage
    from .onenote_resource import OnenoteResource
    from .onenote_section import OnenoteSection
    from .section_group import SectionGroup

from .entity import Entity

@dataclass
class OnenoteEntityBaseModel(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The endpoint where you can get details about the page. Read-only.
    self: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnenoteEntityBaseModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnenoteEntityBaseModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.notebook".casefold():
            from .notebook import Notebook

            return Notebook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntityHierarchyModel".casefold():
            from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel

            return OnenoteEntityHierarchyModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntitySchemaObjectModel".casefold():
            from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel

            return OnenoteEntitySchemaObjectModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenotePage".casefold():
            from .onenote_page import OnenotePage

            return OnenotePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteResource".casefold():
            from .onenote_resource import OnenoteResource

            return OnenoteResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteSection".casefold():
            from .onenote_section import OnenoteSection

            return OnenoteSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sectionGroup".casefold():
            from .section_group import SectionGroup

            return SectionGroup()
        return OnenoteEntityBaseModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .notebook import Notebook
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
        from .onenote_page import OnenotePage
        from .onenote_resource import OnenoteResource
        from .onenote_section import OnenoteSection
        from .section_group import SectionGroup

        from .entity import Entity
        from .notebook import Notebook
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
        from .onenote_page import OnenotePage
        from .onenote_resource import OnenoteResource
        from .onenote_section import OnenoteSection
        from .section_group import SectionGroup

        fields: Dict[str, Callable[[Any], None]] = {
            "self": lambda n : setattr(self, 'self', n.get_str_value()),
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
        writer.write_str_value("self", self.self)
    

