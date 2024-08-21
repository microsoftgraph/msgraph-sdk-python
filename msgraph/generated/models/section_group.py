from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .notebook import Notebook
    from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
    from .onenote_section import OnenoteSection

from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel

@dataclass
class SectionGroup(OnenoteEntityHierarchyModel):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.sectionGroup"
    # The notebook that contains the section group. Read-only.
    parent_notebook: Optional[Notebook] = None
    # The section group that contains the section group. Read-only.
    parent_section_group: Optional[SectionGroup] = None
    # The section groups in the section. Read-only. Nullable.
    section_groups: Optional[List[SectionGroup]] = None
    # The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.
    section_groups_url: Optional[str] = None
    # The sections in the section group. Read-only. Nullable.
    sections: Optional[List[OnenoteSection]] = None
    # The URL for the sections navigation property, which returns all the sections in the section group. Read-only.
    sections_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SectionGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .notebook import Notebook
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_section import OnenoteSection

        from .notebook import Notebook
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_section import OnenoteSection

        fields: Dict[str, Callable[[Any], None]] = {
            "parentNotebook": lambda n : setattr(self, 'parent_notebook', n.get_object_value(Notebook)),
            "parentSectionGroup": lambda n : setattr(self, 'parent_section_group', n.get_object_value(SectionGroup)),
            "sectionGroups": lambda n : setattr(self, 'section_groups', n.get_collection_of_object_values(SectionGroup)),
            "sectionGroupsUrl": lambda n : setattr(self, 'section_groups_url', n.get_str_value()),
            "sections": lambda n : setattr(self, 'sections', n.get_collection_of_object_values(OnenoteSection)),
            "sectionsUrl": lambda n : setattr(self, 'sections_url', n.get_str_value()),
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
        writer.write_object_value("parentNotebook", self.parent_notebook)
        writer.write_object_value("parentSectionGroup", self.parent_section_group)
        writer.write_collection_of_object_values("sectionGroups", self.section_groups)
        writer.write_str_value("sectionGroupsUrl", self.section_groups_url)
        writer.write_collection_of_object_values("sections", self.sections)
        writer.write_str_value("sectionsUrl", self.sections_url)
    

