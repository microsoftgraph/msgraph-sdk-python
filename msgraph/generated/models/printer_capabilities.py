from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .integer_range import IntegerRange
    from .printer_feed_orientation import PrinterFeedOrientation
    from .print_color_mode import PrintColorMode
    from .print_duplex_mode import PrintDuplexMode
    from .print_finishing import PrintFinishing
    from .print_multipage_layout import PrintMultipageLayout
    from .print_orientation import PrintOrientation
    from .print_quality import PrintQuality
    from .print_scaling import PrintScaling

@dataclass
class PrinterCapabilities(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A list of supported bottom margins(in microns) for the printer.
    bottom_margins: Optional[List[int]] = None
    # True if the printer supports collating when printing muliple copies of a multi-page document; false otherwise.
    collation: Optional[bool] = None
    # The color modes supported by the printer. Valid values are described in the following table.
    color_modes: Optional[List[PrintColorMode]] = None
    # A list of supported content (MIME) types that the printer supports. It is not guaranteed that the Universal Print service supports printing all of these MIME types.
    content_types: Optional[List[str]] = None
    # The range of copies per job supported by the printer.
    copies_per_job: Optional[IntegerRange] = None
    # The list of print resolutions in DPI that are supported by the printer.
    dpis: Optional[List[int]] = None
    # The list of duplex modes that are supported by the printer. Valid values are described in the following table.
    duplex_modes: Optional[List[PrintDuplexMode]] = None
    # The list of feed orientations that are supported by the printer.
    feed_orientations: Optional[List[PrinterFeedOrientation]] = None
    # Finishing processes the printer supports for a printed document.
    finishings: Optional[List[PrintFinishing]] = None
    # Supported input bins for the printer.
    input_bins: Optional[List[str]] = None
    # True if color printing is supported by the printer; false otherwise. Read-only.
    is_color_printing_supported: Optional[bool] = None
    # True if the printer supports printing by page ranges; false otherwise.
    is_page_range_supported: Optional[bool] = None
    # A list of supported left margins(in microns) for the printer.
    left_margins: Optional[List[int]] = None
    # The media (i.e., paper) colors supported by the printer.
    media_colors: Optional[List[str]] = None
    # The media sizes supported by the printer. Supports standard size names for ISO and ANSI media sizes. Valid values are in the following table.
    media_sizes: Optional[List[str]] = None
    # The media types supported by the printer.
    media_types: Optional[List[str]] = None
    # The presentation directions supported by the printer. Supported values are described in the following table.
    multipage_layouts: Optional[List[PrintMultipageLayout]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The print orientations supported by the printer. Valid values are described in the following table.
    orientations: Optional[List[PrintOrientation]] = None
    # The printer's supported output bins (trays).
    output_bins: Optional[List[str]] = None
    # Supported number of Input Pages to impose upon a single Impression.
    pages_per_sheet: Optional[List[int]] = None
    # The print qualities supported by the printer.
    qualities: Optional[List[PrintQuality]] = None
    # A list of supported right margins(in microns) for the printer.
    right_margins: Optional[List[int]] = None
    # Supported print scalings.
    scalings: Optional[List[PrintScaling]] = None
    # True if the printer supports scaling PDF pages to match the print media size; false otherwise.
    supports_fit_pdf_to_page: Optional[bool] = None
    # A list of supported top margins(in microns) for the printer.
    top_margins: Optional[List[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterCapabilities:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrinterCapabilities
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrinterCapabilities()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .integer_range import IntegerRange
        from .printer_feed_orientation import PrinterFeedOrientation
        from .print_color_mode import PrintColorMode
        from .print_duplex_mode import PrintDuplexMode
        from .print_finishing import PrintFinishing
        from .print_multipage_layout import PrintMultipageLayout
        from .print_orientation import PrintOrientation
        from .print_quality import PrintQuality
        from .print_scaling import PrintScaling

        from .integer_range import IntegerRange
        from .printer_feed_orientation import PrinterFeedOrientation
        from .print_color_mode import PrintColorMode
        from .print_duplex_mode import PrintDuplexMode
        from .print_finishing import PrintFinishing
        from .print_multipage_layout import PrintMultipageLayout
        from .print_orientation import PrintOrientation
        from .print_quality import PrintQuality
        from .print_scaling import PrintScaling

        fields: Dict[str, Callable[[Any], None]] = {
            "bottom_margins": lambda n : setattr(self, 'bottom_margins', n.get_collection_of_primitive_values(int)),
            "collation": lambda n : setattr(self, 'collation', n.get_bool_value()),
            "color_modes": lambda n : setattr(self, 'color_modes', n.get_collection_of_enum_values(PrintColorMode)),
            "content_types": lambda n : setattr(self, 'content_types', n.get_collection_of_primitive_values(str)),
            "copies_per_job": lambda n : setattr(self, 'copies_per_job', n.get_object_value(IntegerRange)),
            "dpis": lambda n : setattr(self, 'dpis', n.get_collection_of_primitive_values(int)),
            "duplex_modes": lambda n : setattr(self, 'duplex_modes', n.get_collection_of_enum_values(PrintDuplexMode)),
            "feed_orientations": lambda n : setattr(self, 'feed_orientations', n.get_collection_of_enum_values(PrinterFeedOrientation)),
            "finishings": lambda n : setattr(self, 'finishings', n.get_collection_of_enum_values(PrintFinishing)),
            "input_bins": lambda n : setattr(self, 'input_bins', n.get_collection_of_primitive_values(str)),
            "is_color_printing_supported": lambda n : setattr(self, 'is_color_printing_supported', n.get_bool_value()),
            "is_page_range_supported": lambda n : setattr(self, 'is_page_range_supported', n.get_bool_value()),
            "left_margins": lambda n : setattr(self, 'left_margins', n.get_collection_of_primitive_values(int)),
            "media_colors": lambda n : setattr(self, 'media_colors', n.get_collection_of_primitive_values(str)),
            "media_sizes": lambda n : setattr(self, 'media_sizes', n.get_collection_of_primitive_values(str)),
            "media_types": lambda n : setattr(self, 'media_types', n.get_collection_of_primitive_values(str)),
            "multipage_layouts": lambda n : setattr(self, 'multipage_layouts', n.get_collection_of_enum_values(PrintMultipageLayout)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "orientations": lambda n : setattr(self, 'orientations', n.get_collection_of_enum_values(PrintOrientation)),
            "output_bins": lambda n : setattr(self, 'output_bins', n.get_collection_of_primitive_values(str)),
            "pages_per_sheet": lambda n : setattr(self, 'pages_per_sheet', n.get_collection_of_primitive_values(int)),
            "qualities": lambda n : setattr(self, 'qualities', n.get_collection_of_enum_values(PrintQuality)),
            "right_margins": lambda n : setattr(self, 'right_margins', n.get_collection_of_primitive_values(int)),
            "scalings": lambda n : setattr(self, 'scalings', n.get_collection_of_enum_values(PrintScaling)),
            "supports_fit_pdf_to_page": lambda n : setattr(self, 'supports_fit_pdf_to_page', n.get_bool_value()),
            "top_margins": lambda n : setattr(self, 'top_margins', n.get_collection_of_primitive_values(int)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("bottom_margins", self.bottom_margins)
        writer.write_bool_value("collation", self.collation)
        writer.write_collection_of_enum_values("color_modes", self.color_modes)
        writer.write_collection_of_primitive_values("content_types", self.content_types)
        writer.write_object_value("copies_per_job", self.copies_per_job)
        writer.write_collection_of_primitive_values("dpis", self.dpis)
        writer.write_collection_of_enum_values("duplex_modes", self.duplex_modes)
        writer.write_collection_of_enum_values("feed_orientations", self.feed_orientations)
        writer.write_collection_of_enum_values("finishings", self.finishings)
        writer.write_collection_of_primitive_values("input_bins", self.input_bins)
        writer.write_bool_value("is_color_printing_supported", self.is_color_printing_supported)
        writer.write_bool_value("is_page_range_supported", self.is_page_range_supported)
        writer.write_collection_of_primitive_values("left_margins", self.left_margins)
        writer.write_collection_of_primitive_values("media_colors", self.media_colors)
        writer.write_collection_of_primitive_values("media_sizes", self.media_sizes)
        writer.write_collection_of_primitive_values("media_types", self.media_types)
        writer.write_collection_of_enum_values("multipage_layouts", self.multipage_layouts)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_enum_values("orientations", self.orientations)
        writer.write_collection_of_primitive_values("output_bins", self.output_bins)
        writer.write_collection_of_primitive_values("pages_per_sheet", self.pages_per_sheet)
        writer.write_collection_of_enum_values("qualities", self.qualities)
        writer.write_collection_of_primitive_values("right_margins", self.right_margins)
        writer.write_collection_of_enum_values("scalings", self.scalings)
        writer.write_bool_value("supports_fit_pdf_to_page", self.supports_fit_pdf_to_page)
        writer.write_collection_of_primitive_values("top_margins", self.top_margins)
        writer.write_additional_data_value(self.additional_data)
    

