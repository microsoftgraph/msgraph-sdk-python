from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_site_page import BaseSitePage
    from .canvas_layout import CanvasLayout
    from .page_promotion_type import PagePromotionType
    from .reactions_facet import ReactionsFacet
    from .title_area import TitleArea
    from .web_part import WebPart

from .base_site_page import BaseSitePage

@dataclass
class SitePage(BaseSitePage):
    # The canvasLayout property
    canvas_layout: Optional[CanvasLayout] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The promotionKind property
    promotion_kind: Optional[PagePromotionType] = None
    # The reactions property
    reactions: Optional[ReactionsFacet] = None
    # The showComments property
    show_comments: Optional[bool] = None
    # The showRecommendedPages property
    show_recommended_pages: Optional[bool] = None
    # The thumbnailWebUrl property
    thumbnail_web_url: Optional[str] = None
    # The titleArea property
    title_area: Optional[TitleArea] = None
    # The webParts property
    web_parts: Optional[List[WebPart]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SitePage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SitePage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SitePage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_site_page import BaseSitePage
        from .canvas_layout import CanvasLayout
        from .page_promotion_type import PagePromotionType
        from .reactions_facet import ReactionsFacet
        from .title_area import TitleArea
        from .web_part import WebPart

        from .base_site_page import BaseSitePage
        from .canvas_layout import CanvasLayout
        from .page_promotion_type import PagePromotionType
        from .reactions_facet import ReactionsFacet
        from .title_area import TitleArea
        from .web_part import WebPart

        fields: Dict[str, Callable[[Any], None]] = {
            "canvasLayout": lambda n : setattr(self, 'canvas_layout', n.get_object_value(CanvasLayout)),
            "promotionKind": lambda n : setattr(self, 'promotion_kind', n.get_enum_value(PagePromotionType)),
            "reactions": lambda n : setattr(self, 'reactions', n.get_object_value(ReactionsFacet)),
            "showComments": lambda n : setattr(self, 'show_comments', n.get_bool_value()),
            "showRecommendedPages": lambda n : setattr(self, 'show_recommended_pages', n.get_bool_value()),
            "thumbnailWebUrl": lambda n : setattr(self, 'thumbnail_web_url', n.get_str_value()),
            "titleArea": lambda n : setattr(self, 'title_area', n.get_object_value(TitleArea)),
            "webParts": lambda n : setattr(self, 'web_parts', n.get_collection_of_object_values(WebPart)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("canvasLayout", self.canvas_layout)
        writer.write_enum_value("promotionKind", self.promotion_kind)
        writer.write_object_value("reactions", self.reactions)
        writer.write_bool_value("showComments", self.show_comments)
        writer.write_bool_value("showRecommendedPages", self.show_recommended_pages)
        writer.write_str_value("thumbnailWebUrl", self.thumbnail_web_url)
        writer.write_object_value("titleArea", self.title_area)
        writer.write_collection_of_object_values("webParts", self.web_parts)
    

