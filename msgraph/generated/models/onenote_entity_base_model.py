from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

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
class OnenoteEntityBaseModel(Entity, Parsable):
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
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
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
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
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

        fields: dict[str, Callable[[Any], None]] = {
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
    

