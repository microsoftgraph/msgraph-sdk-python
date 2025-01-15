from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .notebook import Notebook
    from .onenote_operation import OnenoteOperation
    from .onenote_page import OnenotePage
    from .onenote_resource import OnenoteResource
    from .onenote_section import OnenoteSection
    from .section_group import SectionGroup

from .entity import Entity

@dataclass
class Onenote(Entity, Parsable):
    # The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.
    notebooks: Optional[list[Notebook]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of OneNote operations. Getting an operations collection isn't supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.
    operations: Optional[list[OnenoteOperation]] = None
    # The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
    pages: Optional[list[OnenotePage]] = None
    # The image and other file resources in OneNote pages. Getting a resources collection isn't supported, but you can get the binary content of a specific resource. Read-only. Nullable.
    resources: Optional[list[OnenoteResource]] = None
    # The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
    section_groups: Optional[list[SectionGroup]] = None
    # The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
    sections: Optional[list[OnenoteSection]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Onenote:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Onenote
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Onenote()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .notebook import Notebook
        from .onenote_operation import OnenoteOperation
        from .onenote_page import OnenotePage
        from .onenote_resource import OnenoteResource
        from .onenote_section import OnenoteSection
        from .section_group import SectionGroup

        from .entity import Entity
        from .notebook import Notebook
        from .onenote_operation import OnenoteOperation
        from .onenote_page import OnenotePage
        from .onenote_resource import OnenoteResource
        from .onenote_section import OnenoteSection
        from .section_group import SectionGroup

        fields: dict[str, Callable[[Any], None]] = {
            "notebooks": lambda n : setattr(self, 'notebooks', n.get_collection_of_object_values(Notebook)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(OnenoteOperation)),
            "pages": lambda n : setattr(self, 'pages', n.get_collection_of_object_values(OnenotePage)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(OnenoteResource)),
            "sectionGroups": lambda n : setattr(self, 'section_groups', n.get_collection_of_object_values(SectionGroup)),
            "sections": lambda n : setattr(self, 'sections', n.get_collection_of_object_values(OnenoteSection)),
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
        writer.write_collection_of_object_values("notebooks", self.notebooks)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("pages", self.pages)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_collection_of_object_values("sectionGroups", self.section_groups)
        writer.write_collection_of_object_values("sections", self.sections)
    

