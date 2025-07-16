from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .integer_range import IntegerRange
    from .printer_feed_orientation import PrinterFeedOrientation
    from .print_color_mode import PrintColorMode
    from .print_duplex_mode import PrintDuplexMode
    from .print_finishing import PrintFinishing
    from .print_margin import PrintMargin
    from .print_multipage_layout import PrintMultipageLayout
    from .print_orientation import PrintOrientation
    from .print_quality import PrintQuality
    from .print_scaling import PrintScaling

@dataclass
class PrintJobConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Whether the printer should collate pages wehen printing multiple copies of a multi-page document.
    collate: Optional[bool] = None
    # The color mode the printer should use to print the job. Valid values are described in the table below. Read-only.
    color_mode: Optional[PrintColorMode] = None
    # The number of copies that should be printed. Read-only.
    copies: Optional[int] = None
    # The resolution to use when printing the job, expressed in dots per inch (DPI). Read-only.
    dpi: Optional[int] = None
    # The duplex mode the printer should use when printing the job. Valid values are described in the table below. Read-only.
    duplex_mode: Optional[PrintDuplexMode] = None
    # The orientation to use when feeding media into the printer. Valid values are described in the following table. Read-only.
    feed_orientation: Optional[PrinterFeedOrientation] = None
    # Finishing processes to use when printing.
    finishings: Optional[list[PrintFinishing]] = None
    # True to fit each page of a PDF document to a physical sheet of media; false to let the printer decide how to lay out impressions.
    fit_pdf_to_page: Optional[bool] = None
    # The input bin (tray) to use when printing. See the printer's capabilities for a list of supported input bins.
    input_bin: Optional[str] = None
    # The margin settings to use when printing.
    margin: Optional[PrintMargin] = None
    # The media size to use when printing. Supports standard size names for ISO and ANSI media sizes. Valid values listed in the printerCapabilities topic.
    media_size: Optional[str] = None
    # The default media (such as paper) type to print the document on.
    media_type: Optional[str] = None
    # The direction to lay out pages when multiple pages are being printed per sheet. Valid values are described in the following table.
    multipage_layout: Optional[PrintMultipageLayout] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The orientation setting the printer should use when printing the job. Valid values are described in the following table.
    orientation: Optional[PrintOrientation] = None
    # The output bin to place completed prints into. See the printer's capabilities for a list of supported output bins.
    output_bin: Optional[str] = None
    # The page ranges to print. Read-only.
    page_ranges: Optional[list[IntegerRange]] = None
    # The number of document pages to print on each sheet.
    pages_per_sheet: Optional[int] = None
    # The print quality to use when printing the job. Valid values are described in the table below. Read-only.
    quality: Optional[PrintQuality] = None
    # Specifies how the printer should scale the document data to fit the requested media. Valid values are described in the following table.
    scaling: Optional[PrintScaling] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrintJobConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrintJobConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrintJobConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .integer_range import IntegerRange
        from .printer_feed_orientation import PrinterFeedOrientation
        from .print_color_mode import PrintColorMode
        from .print_duplex_mode import PrintDuplexMode
        from .print_finishing import PrintFinishing
        from .print_margin import PrintMargin
        from .print_multipage_layout import PrintMultipageLayout
        from .print_orientation import PrintOrientation
        from .print_quality import PrintQuality
        from .print_scaling import PrintScaling

        from .integer_range import IntegerRange
        from .printer_feed_orientation import PrinterFeedOrientation
        from .print_color_mode import PrintColorMode
        from .print_duplex_mode import PrintDuplexMode
        from .print_finishing import PrintFinishing
        from .print_margin import PrintMargin
        from .print_multipage_layout import PrintMultipageLayout
        from .print_orientation import PrintOrientation
        from .print_quality import PrintQuality
        from .print_scaling import PrintScaling

        fields: dict[str, Callable[[Any], None]] = {
            "collate": lambda n : setattr(self, 'collate', n.get_bool_value()),
            "colorMode": lambda n : setattr(self, 'color_mode', n.get_enum_value(PrintColorMode)),
            "copies": lambda n : setattr(self, 'copies', n.get_int_value()),
            "dpi": lambda n : setattr(self, 'dpi', n.get_int_value()),
            "duplexMode": lambda n : setattr(self, 'duplex_mode', n.get_enum_value(PrintDuplexMode)),
            "feedOrientation": lambda n : setattr(self, 'feed_orientation', n.get_enum_value(PrinterFeedOrientation)),
            "finishings": lambda n : setattr(self, 'finishings', n.get_collection_of_enum_values(PrintFinishing)),
            "fitPdfToPage": lambda n : setattr(self, 'fit_pdf_to_page', n.get_bool_value()),
            "inputBin": lambda n : setattr(self, 'input_bin', n.get_str_value()),
            "margin": lambda n : setattr(self, 'margin', n.get_object_value(PrintMargin)),
            "mediaSize": lambda n : setattr(self, 'media_size', n.get_str_value()),
            "mediaType": lambda n : setattr(self, 'media_type', n.get_str_value()),
            "multipageLayout": lambda n : setattr(self, 'multipage_layout', n.get_enum_value(PrintMultipageLayout)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "orientation": lambda n : setattr(self, 'orientation', n.get_enum_value(PrintOrientation)),
            "outputBin": lambda n : setattr(self, 'output_bin', n.get_str_value()),
            "pageRanges": lambda n : setattr(self, 'page_ranges', n.get_collection_of_object_values(IntegerRange)),
            "pagesPerSheet": lambda n : setattr(self, 'pages_per_sheet', n.get_int_value()),
            "quality": lambda n : setattr(self, 'quality', n.get_enum_value(PrintQuality)),
            "scaling": lambda n : setattr(self, 'scaling', n.get_enum_value(PrintScaling)),
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
        writer.write_bool_value("collate", self.collate)
        writer.write_enum_value("colorMode", self.color_mode)
        writer.write_int_value("copies", self.copies)
        writer.write_int_value("dpi", self.dpi)
        writer.write_enum_value("duplexMode", self.duplex_mode)
        writer.write_enum_value("feedOrientation", self.feed_orientation)
        writer.write_collection_of_enum_values("finishings", self.finishings)
        writer.write_bool_value("fitPdfToPage", self.fit_pdf_to_page)
        writer.write_str_value("inputBin", self.input_bin)
        writer.write_object_value("margin", self.margin)
        writer.write_str_value("mediaSize", self.media_size)
        writer.write_str_value("mediaType", self.media_type)
        writer.write_enum_value("multipageLayout", self.multipage_layout)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("orientation", self.orientation)
        writer.write_str_value("outputBin", self.output_bin)
        writer.write_collection_of_object_values("pageRanges", self.page_ranges)
        writer.write_int_value("pagesPerSheet", self.pages_per_sheet)
        writer.write_enum_value("quality", self.quality)
        writer.write_enum_value("scaling", self.scaling)
        writer.write_additional_data_value(self.additional_data)
    

