from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, notebook, onenote_operation, onenote_page, onenote_resource, onenote_section, section_group

from . import entity

@dataclass
class Onenote(entity.Entity):
    # The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.
    notebooks: Optional[List[notebook.Notebook]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.
    operations: Optional[List[onenote_operation.OnenoteOperation]] = None
    # The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
    pages: Optional[List[onenote_page.OnenotePage]] = None
    # The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.
    resources: Optional[List[onenote_resource.OnenoteResource]] = None
    # The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
    section_groups: Optional[List[section_group.SectionGroup]] = None
    # The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
    sections: Optional[List[onenote_section.OnenoteSection]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Onenote:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Onenote
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Onenote()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, notebook, onenote_operation, onenote_page, onenote_resource, onenote_section, section_group

        from . import entity, notebook, onenote_operation, onenote_page, onenote_resource, onenote_section, section_group

        fields: Dict[str, Callable[[Any], None]] = {
            "notebooks": lambda n : setattr(self, 'notebooks', n.get_collection_of_object_values(notebook.Notebook)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(onenote_operation.OnenoteOperation)),
            "pages": lambda n : setattr(self, 'pages', n.get_collection_of_object_values(onenote_page.OnenotePage)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(onenote_resource.OnenoteResource)),
            "sectionGroups": lambda n : setattr(self, 'section_groups', n.get_collection_of_object_values(section_group.SectionGroup)),
            "sections": lambda n : setattr(self, 'sections', n.get_collection_of_object_values(onenote_section.OnenoteSection)),
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
        writer.write_collection_of_object_values("notebooks", self.notebooks)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("pages", self.pages)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_collection_of_object_values("sectionGroups", self.section_groups)
        writer.write_collection_of_object_values("sections", self.sections)
    

