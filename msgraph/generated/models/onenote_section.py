from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

notebook = lazy_import('msgraph.generated.models.notebook')
onenote_entity_hierarchy_model = lazy_import('msgraph.generated.models.onenote_entity_hierarchy_model')
onenote_page = lazy_import('msgraph.generated.models.onenote_page')
section_group = lazy_import('msgraph.generated.models.section_group')
section_links = lazy_import('msgraph.generated.models.section_links')

class OnenoteSection(onenote_entity_hierarchy_model.OnenoteEntityHierarchyModel):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new onenoteSection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.onenoteSection"
        # Indicates whether this is the user's default section. Read-only.
        self._is_default: Optional[bool] = None
        # Links for opening the section. The oneNoteClientURL link opens the section in the OneNote native client if it's installed. The oneNoteWebURL link opens the section in OneNote on the web.
        self._links: Optional[section_links.SectionLinks] = None
        # The collection of pages in the section.  Read-only. Nullable.
        self._pages: Optional[List[onenote_page.OnenotePage]] = None
        # The pages endpoint where you can get details for all the pages in the section. Read-only.
        self._pages_url: Optional[str] = None
        # The notebook that contains the section.  Read-only.
        self._parent_notebook: Optional[notebook.Notebook] = None
        # The section group that contains the section.  Read-only.
        self._parent_section_group: Optional[section_group.SectionGroup] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnenoteSection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnenoteSection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnenoteSection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(section_links.SectionLinks)),
            "pages": lambda n : setattr(self, 'pages', n.get_collection_of_object_values(onenote_page.OnenotePage)),
            "pages_url": lambda n : setattr(self, 'pages_url', n.get_str_value()),
            "parent_notebook": lambda n : setattr(self, 'parent_notebook', n.get_object_value(notebook.Notebook)),
            "parent_section_group": lambda n : setattr(self, 'parent_section_group', n.get_object_value(section_group.SectionGroup)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. Indicates whether this is the user's default section. Read-only.
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. Indicates whether this is the user's default section. Read-only.
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def links(self,) -> Optional[section_links.SectionLinks]:
        """
        Gets the links property value. Links for opening the section. The oneNoteClientURL link opens the section in the OneNote native client if it's installed. The oneNoteWebURL link opens the section in OneNote on the web.
        Returns: Optional[section_links.SectionLinks]
        """
        return self._links
    
    @links.setter
    def links(self,value: Optional[section_links.SectionLinks] = None) -> None:
        """
        Sets the links property value. Links for opening the section. The oneNoteClientURL link opens the section in the OneNote native client if it's installed. The oneNoteWebURL link opens the section in OneNote on the web.
        Args:
            value: Value to set for the links property.
        """
        self._links = value
    
    @property
    def pages(self,) -> Optional[List[onenote_page.OnenotePage]]:
        """
        Gets the pages property value. The collection of pages in the section.  Read-only. Nullable.
        Returns: Optional[List[onenote_page.OnenotePage]]
        """
        return self._pages
    
    @pages.setter
    def pages(self,value: Optional[List[onenote_page.OnenotePage]] = None) -> None:
        """
        Sets the pages property value. The collection of pages in the section.  Read-only. Nullable.
        Args:
            value: Value to set for the pages property.
        """
        self._pages = value
    
    @property
    def pages_url(self,) -> Optional[str]:
        """
        Gets the pagesUrl property value. The pages endpoint where you can get details for all the pages in the section. Read-only.
        Returns: Optional[str]
        """
        return self._pages_url
    
    @pages_url.setter
    def pages_url(self,value: Optional[str] = None) -> None:
        """
        Sets the pagesUrl property value. The pages endpoint where you can get details for all the pages in the section. Read-only.
        Args:
            value: Value to set for the pagesUrl property.
        """
        self._pages_url = value
    
    @property
    def parent_notebook(self,) -> Optional[notebook.Notebook]:
        """
        Gets the parentNotebook property value. The notebook that contains the section.  Read-only.
        Returns: Optional[notebook.Notebook]
        """
        return self._parent_notebook
    
    @parent_notebook.setter
    def parent_notebook(self,value: Optional[notebook.Notebook] = None) -> None:
        """
        Sets the parentNotebook property value. The notebook that contains the section.  Read-only.
        Args:
            value: Value to set for the parentNotebook property.
        """
        self._parent_notebook = value
    
    @property
    def parent_section_group(self,) -> Optional[section_group.SectionGroup]:
        """
        Gets the parentSectionGroup property value. The section group that contains the section.  Read-only.
        Returns: Optional[section_group.SectionGroup]
        """
        return self._parent_section_group
    
    @parent_section_group.setter
    def parent_section_group(self,value: Optional[section_group.SectionGroup] = None) -> None:
        """
        Sets the parentSectionGroup property value. The section group that contains the section.  Read-only.
        Args:
            value: Value to set for the parentSectionGroup property.
        """
        self._parent_section_group = value
    
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
        writer.write_object_value("links", self.links)
        writer.write_collection_of_object_values("pages", self.pages)
        writer.write_str_value("pagesUrl", self.pages_url)
        writer.write_object_value("parentNotebook", self.parent_notebook)
        writer.write_object_value("parentSectionGroup", self.parent_section_group)
    

