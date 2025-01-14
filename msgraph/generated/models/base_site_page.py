from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_item import BaseItem
    from .page_layout_type import PageLayoutType
    from .publication_facet import PublicationFacet
    from .site_page import SitePage

from .base_item import BaseItem

@dataclass
class BaseSitePage(BaseItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.baseSitePage"
    # The name of the page layout of the page. The possible values are: microsoftReserved, article, home, unknownFutureValue.
    page_layout: Optional[PageLayoutType] = None
    # The publishing status and the MM.mm version of the page.
    publishing_state: Optional[PublicationFacet] = None
    # Title of the sitePage.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BaseSitePage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseSitePage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sitePage".casefold():
            from .site_page import SitePage

            return SitePage()
        return BaseSitePage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_item import BaseItem
        from .page_layout_type import PageLayoutType
        from .publication_facet import PublicationFacet
        from .site_page import SitePage

        from .base_item import BaseItem
        from .page_layout_type import PageLayoutType
        from .publication_facet import PublicationFacet
        from .site_page import SitePage

        fields: dict[str, Callable[[Any], None]] = {
            "pageLayout": lambda n : setattr(self, 'page_layout', n.get_enum_value(PageLayoutType)),
            "publishingState": lambda n : setattr(self, 'publishing_state', n.get_object_value(PublicationFacet)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_enum_value("pageLayout", self.page_layout)
        writer.write_object_value("publishingState", self.publishing_state)
        writer.write_str_value("title", self.title)
    

