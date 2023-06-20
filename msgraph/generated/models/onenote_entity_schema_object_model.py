from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import notebook, onenote_entity_base_model, onenote_entity_hierarchy_model, onenote_page, onenote_section, section_group

from . import onenote_entity_base_model

@dataclass
class OnenoteEntitySchemaObjectModel(onenote_entity_base_model.OnenoteEntityBaseModel):
    odata_type = "#microsoft.graph.onenoteEntitySchemaObjectModel"
    # The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnenoteEntitySchemaObjectModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnenoteEntitySchemaObjectModel
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenotePage".casefold():
            from . import onenote_page

            return onenote_page.OnenotePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteSection".casefold():
            from . import onenote_section

            return onenote_section.OnenoteSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sectionGroup".casefold():
            from . import section_group

            return section_group.SectionGroup()
        return OnenoteEntitySchemaObjectModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import notebook, onenote_entity_base_model, onenote_entity_hierarchy_model, onenote_page, onenote_section, section_group

        from . import notebook, onenote_entity_base_model, onenote_entity_hierarchy_model, onenote_page, onenote_section, section_group

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
    

