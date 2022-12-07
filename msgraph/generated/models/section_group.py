from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

notebook = lazy_import('msgraph.generated.models.notebook')
onenote_entity_hierarchy_model = lazy_import('msgraph.generated.models.onenote_entity_hierarchy_model')
onenote_section = lazy_import('msgraph.generated.models.onenote_section')

class SectionGroup(onenote_entity_hierarchy_model.OnenoteEntityHierarchyModel):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new sectionGroup and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.sectionGroup"
        # The notebook that contains the section group. Read-only.
        self._parent_notebook: Optional[notebook.Notebook] = None
        # The section group that contains the section group. Read-only.
        self._parent_section_group: Optional[SectionGroup] = None
        # The section groups in the section. Read-only. Nullable.
        self._section_groups: Optional[List[SectionGroup]] = None
        # The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.
        self._section_groups_url: Optional[str] = None
        # The sections in the section group. Read-only. Nullable.
        self._sections: Optional[List[onenote_section.OnenoteSection]] = None
        # The URL for the sections navigation property, which returns all the sections in the section group. Read-only.
        self._sections_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SectionGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SectionGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SectionGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "parent_notebook": lambda n : setattr(self, 'parent_notebook', n.get_object_value(notebook.Notebook)),
            "parent_section_group": lambda n : setattr(self, 'parent_section_group', n.get_object_value(SectionGroup)),
            "section_groups": lambda n : setattr(self, 'section_groups', n.get_collection_of_object_values(SectionGroup)),
            "section_groups_url": lambda n : setattr(self, 'section_groups_url', n.get_str_value()),
            "sections": lambda n : setattr(self, 'sections', n.get_collection_of_object_values(onenote_section.OnenoteSection)),
            "sections_url": lambda n : setattr(self, 'sections_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def parent_notebook(self,) -> Optional[notebook.Notebook]:
        """
        Gets the parentNotebook property value. The notebook that contains the section group. Read-only.
        Returns: Optional[notebook.Notebook]
        """
        return self._parent_notebook
    
    @parent_notebook.setter
    def parent_notebook(self,value: Optional[notebook.Notebook] = None) -> None:
        """
        Sets the parentNotebook property value. The notebook that contains the section group. Read-only.
        Args:
            value: Value to set for the parentNotebook property.
        """
        self._parent_notebook = value
    
    @property
    def parent_section_group(self,) -> Optional[SectionGroup]:
        """
        Gets the parentSectionGroup property value. The section group that contains the section group. Read-only.
        Returns: Optional[SectionGroup]
        """
        return self._parent_section_group
    
    @parent_section_group.setter
    def parent_section_group(self,value: Optional[SectionGroup] = None) -> None:
        """
        Sets the parentSectionGroup property value. The section group that contains the section group. Read-only.
        Args:
            value: Value to set for the parentSectionGroup property.
        """
        self._parent_section_group = value
    
    @property
    def section_groups(self,) -> Optional[List[SectionGroup]]:
        """
        Gets the sectionGroups property value. The section groups in the section. Read-only. Nullable.
        Returns: Optional[List[SectionGroup]]
        """
        return self._section_groups
    
    @section_groups.setter
    def section_groups(self,value: Optional[List[SectionGroup]] = None) -> None:
        """
        Sets the sectionGroups property value. The section groups in the section. Read-only. Nullable.
        Args:
            value: Value to set for the sectionGroups property.
        """
        self._section_groups = value
    
    @property
    def section_groups_url(self,) -> Optional[str]:
        """
        Gets the sectionGroupsUrl property value. The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.
        Returns: Optional[str]
        """
        return self._section_groups_url
    
    @section_groups_url.setter
    def section_groups_url(self,value: Optional[str] = None) -> None:
        """
        Sets the sectionGroupsUrl property value. The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.
        Args:
            value: Value to set for the sectionGroupsUrl property.
        """
        self._section_groups_url = value
    
    @property
    def sections(self,) -> Optional[List[onenote_section.OnenoteSection]]:
        """
        Gets the sections property value. The sections in the section group. Read-only. Nullable.
        Returns: Optional[List[onenote_section.OnenoteSection]]
        """
        return self._sections
    
    @sections.setter
    def sections(self,value: Optional[List[onenote_section.OnenoteSection]] = None) -> None:
        """
        Sets the sections property value. The sections in the section group. Read-only. Nullable.
        Args:
            value: Value to set for the sections property.
        """
        self._sections = value
    
    @property
    def sections_url(self,) -> Optional[str]:
        """
        Gets the sectionsUrl property value. The URL for the sections navigation property, which returns all the sections in the section group. Read-only.
        Returns: Optional[str]
        """
        return self._sections_url
    
    @sections_url.setter
    def sections_url(self,value: Optional[str] = None) -> None:
        """
        Sets the sectionsUrl property value. The URL for the sections navigation property, which returns all the sections in the section group. Read-only.
        Args:
            value: Value to set for the sectionsUrl property.
        """
        self._sections_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("parentNotebook", self.parent_notebook)
        writer.write_object_value("parentSectionGroup", self.parent_section_group)
        writer.write_collection_of_object_values("sectionGroups", self.section_groups)
        writer.write_str_value("sectionGroupsUrl", self.section_groups_url)
        writer.write_collection_of_object_values("sections", self.sections)
        writer.write_str_value("sectionsUrl", self.sections_url)
    

