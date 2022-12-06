from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
notebook = lazy_import('msgraph.generated.models.notebook')
onenote_operation = lazy_import('msgraph.generated.models.onenote_operation')
onenote_page = lazy_import('msgraph.generated.models.onenote_page')
onenote_resource = lazy_import('msgraph.generated.models.onenote_resource')
onenote_section = lazy_import('msgraph.generated.models.onenote_section')
section_group = lazy_import('msgraph.generated.models.section_group')

class Onenote(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new onenote and sets the default values.
        """
        super().__init__()
        # The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.
        self._notebooks: Optional[List[notebook.Notebook]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.
        self._operations: Optional[List[onenote_operation.OnenoteOperation]] = None
        # The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        self._pages: Optional[List[onenote_page.OnenotePage]] = None
        # The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.
        self._resources: Optional[List[onenote_resource.OnenoteResource]] = None
        # The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        self._section_groups: Optional[List[section_group.SectionGroup]] = None
        # The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        self._sections: Optional[List[onenote_section.OnenoteSection]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Onenote:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Onenote
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Onenote()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "notebooks": lambda n : setattr(self, 'notebooks', n.get_collection_of_object_values(notebook.Notebook)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(onenote_operation.OnenoteOperation)),
            "pages": lambda n : setattr(self, 'pages', n.get_collection_of_object_values(onenote_page.OnenotePage)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(onenote_resource.OnenoteResource)),
            "section_groups": lambda n : setattr(self, 'section_groups', n.get_collection_of_object_values(section_group.SectionGroup)),
            "sections": lambda n : setattr(self, 'sections', n.get_collection_of_object_values(onenote_section.OnenoteSection)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def notebooks(self,) -> Optional[List[notebook.Notebook]]:
        """
        Gets the notebooks property value. The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.
        Returns: Optional[List[notebook.Notebook]]
        """
        return self._notebooks
    
    @notebooks.setter
    def notebooks(self,value: Optional[List[notebook.Notebook]] = None) -> None:
        """
        Sets the notebooks property value. The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.
        Args:
            value: Value to set for the notebooks property.
        """
        self._notebooks = value
    
    @property
    def operations(self,) -> Optional[List[onenote_operation.OnenoteOperation]]:
        """
        Gets the operations property value. The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.
        Returns: Optional[List[onenote_operation.OnenoteOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[onenote_operation.OnenoteOperation]] = None) -> None:
        """
        Sets the operations property value. The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def pages(self,) -> Optional[List[onenote_page.OnenotePage]]:
        """
        Gets the pages property value. The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        Returns: Optional[List[onenote_page.OnenotePage]]
        """
        return self._pages
    
    @pages.setter
    def pages(self,value: Optional[List[onenote_page.OnenotePage]] = None) -> None:
        """
        Sets the pages property value. The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        Args:
            value: Value to set for the pages property.
        """
        self._pages = value
    
    @property
    def resources(self,) -> Optional[List[onenote_resource.OnenoteResource]]:
        """
        Gets the resources property value. The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.
        Returns: Optional[List[onenote_resource.OnenoteResource]]
        """
        return self._resources
    
    @resources.setter
    def resources(self,value: Optional[List[onenote_resource.OnenoteResource]] = None) -> None:
        """
        Sets the resources property value. The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.
        Args:
            value: Value to set for the resources property.
        """
        self._resources = value
    
    @property
    def section_groups(self,) -> Optional[List[section_group.SectionGroup]]:
        """
        Gets the sectionGroups property value. The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        Returns: Optional[List[section_group.SectionGroup]]
        """
        return self._section_groups
    
    @section_groups.setter
    def section_groups(self,value: Optional[List[section_group.SectionGroup]] = None) -> None:
        """
        Sets the sectionGroups property value. The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        Args:
            value: Value to set for the sectionGroups property.
        """
        self._section_groups = value
    
    @property
    def sections(self,) -> Optional[List[onenote_section.OnenoteSection]]:
        """
        Gets the sections property value. The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        Returns: Optional[List[onenote_section.OnenoteSection]]
        """
        return self._sections
    
    @sections.setter
    def sections(self,value: Optional[List[onenote_section.OnenoteSection]] = None) -> None:
        """
        Sets the sections property value. The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        Args:
            value: Value to set for the sections property.
        """
        self._sections = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("notebooks", self.notebooks)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("pages", self.pages)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_collection_of_object_values("sectionGroups", self.section_groups)
        writer.write_collection_of_object_values("sections", self.sections)
    

