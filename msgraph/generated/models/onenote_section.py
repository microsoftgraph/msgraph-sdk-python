from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .notebook import Notebook
    from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
    from .onenote_page import OnenotePage
    from .section_group import SectionGroup
    from .section_links import SectionLinks

from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel

@dataclass
class OnenoteSection(OnenoteEntityHierarchyModel, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onenoteSection"
    # Indicates whether this is the user's default section. Read-only.
    is_default: Optional[bool] = None
    # Links for opening the section. The oneNoteClientURL link opens the section in the OneNote native client if it's installed. The oneNoteWebURL link opens the section in OneNote on the web.
    links: Optional[SectionLinks] = None
    # The collection of pages in the section.  Read-only. Nullable.
    pages: Optional[list[OnenotePage]] = None
    # The pages endpoint where you can get details for all the pages in the section. Read-only.
    pages_url: Optional[str] = None
    # The notebook that contains the section.  Read-only.
    parent_notebook: Optional[Notebook] = None
    # The section group that contains the section.  Read-only.
    parent_section_group: Optional[SectionGroup] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnenoteSection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnenoteSection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnenoteSection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .notebook import Notebook
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_page import OnenotePage
        from .section_group import SectionGroup
        from .section_links import SectionLinks

        from .notebook import Notebook
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_page import OnenotePage
        from .section_group import SectionGroup
        from .section_links import SectionLinks

        fields: dict[str, Callable[[Any], None]] = {
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(SectionLinks)),
            "pages": lambda n : setattr(self, 'pages', n.get_collection_of_object_values(OnenotePage)),
            "pagesUrl": lambda n : setattr(self, 'pages_url', n.get_str_value()),
            "parentNotebook": lambda n : setattr(self, 'parent_notebook', n.get_object_value(Notebook)),
            "parentSectionGroup": lambda n : setattr(self, 'parent_section_group', n.get_object_value(SectionGroup)),
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
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_object_value("links", self.links)
        writer.write_collection_of_object_values("pages", self.pages)
        writer.write_str_value("pagesUrl", self.pages_url)
        writer.write_object_value("parentNotebook", self.parent_notebook)
        writer.write_object_value("parentSectionGroup", self.parent_section_group)
    

