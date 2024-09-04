from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .server_processed_content import ServerProcessedContent
    from .title_area_layout_type import TitleAreaLayoutType
    from .title_area_text_alignment_type import TitleAreaTextAlignmentType

@dataclass
class TitleArea(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Alternative text on the title area.
    alternative_text: Optional[str] = None
    # Indicates whether the title area has a gradient effect enabled.
    enable_gradient_effect: Optional[bool] = None
    # URL of the image in the title area.
    image_web_url: Optional[str] = None
    # Enumeration value that indicates the layout of the title area. The possible values are: imageAndTitle, plain, colorBlock, overlap, unknownFutureValue.
    layout: Optional[TitleAreaLayoutType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains collections of data that can be processed by server side services like search index and link fixup.
    server_processed_content: Optional[ServerProcessedContent] = None
    # Indicates whether the author should be shown in title area.
    show_author: Optional[bool] = None
    # Indicates whether the published date should be shown in title area.
    show_published_date: Optional[bool] = None
    # Indicates whether the text block above title should be shown in title area.
    show_text_block_above_title: Optional[bool] = None
    # The text above title line.
    text_above_title: Optional[str] = None
    # Enumeration value that indicates the text alignment of the title area. The possible values are: left, center, unknownFutureValue.
    text_alignment: Optional[TitleAreaTextAlignmentType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TitleArea:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TitleArea
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TitleArea()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .server_processed_content import ServerProcessedContent
        from .title_area_layout_type import TitleAreaLayoutType
        from .title_area_text_alignment_type import TitleAreaTextAlignmentType

        from .server_processed_content import ServerProcessedContent
        from .title_area_layout_type import TitleAreaLayoutType
        from .title_area_text_alignment_type import TitleAreaTextAlignmentType

        fields: Dict[str, Callable[[Any], None]] = {
            "alternativeText": lambda n : setattr(self, 'alternative_text', n.get_str_value()),
            "enableGradientEffect": lambda n : setattr(self, 'enable_gradient_effect', n.get_bool_value()),
            "imageWebUrl": lambda n : setattr(self, 'image_web_url', n.get_str_value()),
            "layout": lambda n : setattr(self, 'layout', n.get_enum_value(TitleAreaLayoutType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serverProcessedContent": lambda n : setattr(self, 'server_processed_content', n.get_object_value(ServerProcessedContent)),
            "showAuthor": lambda n : setattr(self, 'show_author', n.get_bool_value()),
            "showPublishedDate": lambda n : setattr(self, 'show_published_date', n.get_bool_value()),
            "showTextBlockAboveTitle": lambda n : setattr(self, 'show_text_block_above_title', n.get_bool_value()),
            "textAboveTitle": lambda n : setattr(self, 'text_above_title', n.get_str_value()),
            "textAlignment": lambda n : setattr(self, 'text_alignment', n.get_enum_value(TitleAreaTextAlignmentType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("alternativeText", self.alternative_text)
        writer.write_bool_value("enableGradientEffect", self.enable_gradient_effect)
        writer.write_str_value("imageWebUrl", self.image_web_url)
        writer.write_enum_value("layout", self.layout)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("serverProcessedContent", self.server_processed_content)
        writer.write_bool_value("showAuthor", self.show_author)
        writer.write_bool_value("showPublishedDate", self.show_published_date)
        writer.write_bool_value("showTextBlockAboveTitle", self.show_text_block_above_title)
        writer.write_str_value("textAboveTitle", self.text_above_title)
        writer.write_enum_value("textAlignment", self.text_alignment)
        writer.write_additional_data_value(self.additional_data)
    

