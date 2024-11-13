from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .notebook import Notebook
    from .onenote_entity_base_model import OnenoteEntityBaseModel
    from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
    from .onenote_page import OnenotePage
    from .onenote_section import OnenoteSection
    from .section_group import SectionGroup

from .onenote_entity_base_model import OnenoteEntityBaseModel

@dataclass
class OnenoteEntitySchemaObjectModel(OnenoteEntityBaseModel, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onenoteEntitySchemaObjectModel"
    # The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnenoteEntitySchemaObjectModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnenoteEntitySchemaObjectModel
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenotePage".casefold():
            from .onenote_page import OnenotePage

            return OnenotePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteSection".casefold():
            from .onenote_section import OnenoteSection

            return OnenoteSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sectionGroup".casefold():
            from .section_group import SectionGroup

            return SectionGroup()
        return OnenoteEntitySchemaObjectModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .notebook import Notebook
        from .onenote_entity_base_model import OnenoteEntityBaseModel
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_page import OnenotePage
        from .onenote_section import OnenoteSection
        from .section_group import SectionGroup

        from .notebook import Notebook
        from .onenote_entity_base_model import OnenoteEntityBaseModel
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_page import OnenotePage
        from .onenote_section import OnenoteSection
        from .section_group import SectionGroup

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
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
        from .notebook import Notebook
        from .onenote_entity_base_model import OnenoteEntityBaseModel
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_page import OnenotePage
        from .onenote_section import OnenoteSection
        from .section_group import SectionGroup

        writer.write_datetime_value("createdDateTime", self.created_date_time)
    

