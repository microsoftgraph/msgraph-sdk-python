from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import notebook_links, onenote_entity_hierarchy_model, onenote_section, onenote_user_role, section_group

from . import onenote_entity_hierarchy_model

@dataclass
class Notebook(onenote_entity_hierarchy_model.OnenoteEntityHierarchyModel):
    odata_type = "#microsoft.graph.notebook"
    # Indicates whether this is the user's default notebook. Read-only.
    is_default: Optional[bool] = None
    # Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.
    is_shared: Optional[bool] = None
    # Links for opening the notebook. The oneNoteClientURL link opens the notebook in the OneNote native client if it's installed. The oneNoteWebURL link opens the notebook in OneNote on the web.
    links: Optional[notebook_links.NotebookLinks] = None
    # The section groups in the notebook. Read-only. Nullable.
    section_groups: Optional[List[section_group.SectionGroup]] = None
    # The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.
    section_groups_url: Optional[str] = None
    # The sections in the notebook. Read-only. Nullable.
    sections: Optional[List[onenote_section.OnenoteSection]] = None
    # The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.
    sections_url: Optional[str] = None
    # Possible values are: Owner, Contributor, Reader, None. Owner represents owner-level access to the notebook. Contributor represents read/write access to the notebook. Reader represents read-only access to the notebook. Read-only.
    user_role: Optional[onenote_user_role.OnenoteUserRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Notebook:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Notebook
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Notebook()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import notebook_links, onenote_entity_hierarchy_model, onenote_section, onenote_user_role, section_group

        from . import notebook_links, onenote_entity_hierarchy_model, onenote_section, onenote_user_role, section_group

        fields: Dict[str, Callable[[Any], None]] = {
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "isShared": lambda n : setattr(self, 'is_shared', n.get_bool_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(notebook_links.NotebookLinks)),
            "sectionGroups": lambda n : setattr(self, 'section_groups', n.get_collection_of_object_values(section_group.SectionGroup)),
            "sectionGroupsUrl": lambda n : setattr(self, 'section_groups_url', n.get_str_value()),
            "sections": lambda n : setattr(self, 'sections', n.get_collection_of_object_values(onenote_section.OnenoteSection)),
            "sectionsUrl": lambda n : setattr(self, 'sections_url', n.get_str_value()),
            "userRole": lambda n : setattr(self, 'user_role', n.get_enum_value(onenote_user_role.OnenoteUserRole)),
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
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isShared", self.is_shared)
        writer.write_object_value("links", self.links)
        writer.write_collection_of_object_values("sectionGroups", self.section_groups)
        writer.write_str_value("sectionGroupsUrl", self.section_groups_url)
        writer.write_collection_of_object_values("sections", self.sections)
        writer.write_str_value("sectionsUrl", self.sections_url)
        writer.write_enum_value("userRole", self.user_role)
    

