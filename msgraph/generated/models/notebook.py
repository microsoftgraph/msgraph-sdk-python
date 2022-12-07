from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

notebook_links = lazy_import('msgraph.generated.models.notebook_links')
onenote_entity_hierarchy_model = lazy_import('msgraph.generated.models.onenote_entity_hierarchy_model')
onenote_section = lazy_import('msgraph.generated.models.onenote_section')
onenote_user_role = lazy_import('msgraph.generated.models.onenote_user_role')
section_group = lazy_import('msgraph.generated.models.section_group')

class Notebook(onenote_entity_hierarchy_model.OnenoteEntityHierarchyModel):
    def __init__(self,) -> None:
        """
        Instantiates a new Notebook and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.notebook"
        # Indicates whether this is the user's default notebook. Read-only.
        self._is_default: Optional[bool] = None
        # Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.
        self._is_shared: Optional[bool] = None
        # Links for opening the notebook. The oneNoteClientURL link opens the notebook in the OneNote native client if it's installed. The oneNoteWebURL link opens the notebook in OneNote on the web.
        self._links: Optional[notebook_links.NotebookLinks] = None
        # The section groups in the notebook. Read-only. Nullable.
        self._section_groups: Optional[List[section_group.SectionGroup]] = None
        # The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.
        self._section_groups_url: Optional[str] = None
        # The sections in the notebook. Read-only. Nullable.
        self._sections: Optional[List[onenote_section.OnenoteSection]] = None
        # The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.
        self._sections_url: Optional[str] = None
        # Possible values are: Owner, Contributor, Reader, None. Owner represents owner-level access to the notebook. Contributor represents read/write access to the notebook. Reader represents read-only access to the notebook. Read-only.
        self._user_role: Optional[onenote_user_role.OnenoteUserRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Notebook:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Notebook
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Notebook()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "is_shared": lambda n : setattr(self, 'is_shared', n.get_bool_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(notebook_links.NotebookLinks)),
            "section_groups": lambda n : setattr(self, 'section_groups', n.get_collection_of_object_values(section_group.SectionGroup)),
            "section_groups_url": lambda n : setattr(self, 'section_groups_url', n.get_str_value()),
            "sections": lambda n : setattr(self, 'sections', n.get_collection_of_object_values(onenote_section.OnenoteSection)),
            "sections_url": lambda n : setattr(self, 'sections_url', n.get_str_value()),
            "user_role": lambda n : setattr(self, 'user_role', n.get_enum_value(onenote_user_role.OnenoteUserRole)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. Indicates whether this is the user's default notebook. Read-only.
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. Indicates whether this is the user's default notebook. Read-only.
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def is_shared(self,) -> Optional[bool]:
        """
        Gets the isShared property value. Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.
        Returns: Optional[bool]
        """
        return self._is_shared
    
    @is_shared.setter
    def is_shared(self,value: Optional[bool] = None) -> None:
        """
        Sets the isShared property value. Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.
        Args:
            value: Value to set for the isShared property.
        """
        self._is_shared = value
    
    @property
    def links(self,) -> Optional[notebook_links.NotebookLinks]:
        """
        Gets the links property value. Links for opening the notebook. The oneNoteClientURL link opens the notebook in the OneNote native client if it's installed. The oneNoteWebURL link opens the notebook in OneNote on the web.
        Returns: Optional[notebook_links.NotebookLinks]
        """
        return self._links
    
    @links.setter
    def links(self,value: Optional[notebook_links.NotebookLinks] = None) -> None:
        """
        Sets the links property value. Links for opening the notebook. The oneNoteClientURL link opens the notebook in the OneNote native client if it's installed. The oneNoteWebURL link opens the notebook in OneNote on the web.
        Args:
            value: Value to set for the links property.
        """
        self._links = value
    
    @property
    def section_groups(self,) -> Optional[List[section_group.SectionGroup]]:
        """
        Gets the sectionGroups property value. The section groups in the notebook. Read-only. Nullable.
        Returns: Optional[List[section_group.SectionGroup]]
        """
        return self._section_groups
    
    @section_groups.setter
    def section_groups(self,value: Optional[List[section_group.SectionGroup]] = None) -> None:
        """
        Sets the sectionGroups property value. The section groups in the notebook. Read-only. Nullable.
        Args:
            value: Value to set for the sectionGroups property.
        """
        self._section_groups = value
    
    @property
    def section_groups_url(self,) -> Optional[str]:
        """
        Gets the sectionGroupsUrl property value. The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.
        Returns: Optional[str]
        """
        return self._section_groups_url
    
    @section_groups_url.setter
    def section_groups_url(self,value: Optional[str] = None) -> None:
        """
        Sets the sectionGroupsUrl property value. The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.
        Args:
            value: Value to set for the sectionGroupsUrl property.
        """
        self._section_groups_url = value
    
    @property
    def sections(self,) -> Optional[List[onenote_section.OnenoteSection]]:
        """
        Gets the sections property value. The sections in the notebook. Read-only. Nullable.
        Returns: Optional[List[onenote_section.OnenoteSection]]
        """
        return self._sections
    
    @sections.setter
    def sections(self,value: Optional[List[onenote_section.OnenoteSection]] = None) -> None:
        """
        Sets the sections property value. The sections in the notebook. Read-only. Nullable.
        Args:
            value: Value to set for the sections property.
        """
        self._sections = value
    
    @property
    def sections_url(self,) -> Optional[str]:
        """
        Gets the sectionsUrl property value. The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.
        Returns: Optional[str]
        """
        return self._sections_url
    
    @sections_url.setter
    def sections_url(self,value: Optional[str] = None) -> None:
        """
        Sets the sectionsUrl property value. The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.
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
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isShared", self.is_shared)
        writer.write_object_value("links", self.links)
        writer.write_collection_of_object_values("sectionGroups", self.section_groups)
        writer.write_str_value("sectionGroupsUrl", self.section_groups_url)
        writer.write_collection_of_object_values("sections", self.sections)
        writer.write_str_value("sectionsUrl", self.sections_url)
        writer.write_enum_value("userRole", self.user_role)
    
    @property
    def user_role(self,) -> Optional[onenote_user_role.OnenoteUserRole]:
        """
        Gets the userRole property value. Possible values are: Owner, Contributor, Reader, None. Owner represents owner-level access to the notebook. Contributor represents read/write access to the notebook. Reader represents read-only access to the notebook. Read-only.
        Returns: Optional[onenote_user_role.OnenoteUserRole]
        """
        return self._user_role
    
    @user_role.setter
    def user_role(self,value: Optional[onenote_user_role.OnenoteUserRole] = None) -> None:
        """
        Sets the userRole property value. Possible values are: Owner, Contributor, Reader, None. Owner represents owner-level access to the notebook. Contributor represents read/write access to the notebook. Reader represents read-only access to the notebook. Read-only.
        Args:
            value: Value to set for the userRole property.
        """
        self._user_role = value
    

