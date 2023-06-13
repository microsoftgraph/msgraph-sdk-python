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
            if mapping_value == "#microsoft.graph.onenotePage":
                from . import onenote_page

                return onenote_page.OnenotePage()
            if mapping_value == "#microsoft.graph.onenoteSection":
                from . import onenote_section

                return onenote_section.OnenoteSection()
            if mapping_value == "#microsoft.graph.sectionGroup":
                from . import section_group

                return section_group.SectionGroup()
        return OnenoteEntitySchemaObjectModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
    

