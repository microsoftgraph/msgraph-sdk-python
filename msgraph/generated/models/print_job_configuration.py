from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import integer_range, printer_feed_orientation, print_color_mode, print_duplex_mode, print_finishing, print_margin, print_multipage_layout, print_orientation, print_quality, print_scaling

@dataclass
class PrintJobConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Whether the printer should collate pages wehen printing multiple copies of a multi-page document.
    collate: Optional[bool] = None
    # The color mode the printer should use to print the job. Valid values are described in the table below. Read-only.
    color_mode: Optional[print_color_mode.PrintColorMode] = None
    # The number of copies that should be printed. Read-only.
    copies: Optional[int] = None
    # The resolution to use when printing the job, expressed in dots per inch (DPI). Read-only.
    dpi: Optional[int] = None
    # The duplex mode the printer should use when printing the job. Valid values are described in the table below. Read-only.
    duplex_mode: Optional[print_duplex_mode.PrintDuplexMode] = None
    # The orientation to use when feeding media into the printer. Valid values are described in the following table. Read-only.
    feed_orientation: Optional[printer_feed_orientation.PrinterFeedOrientation] = None
    # Finishing processes to use when printing.
    finishings: Optional[List[print_finishing.PrintFinishing]] = None
    # The fitPdfToPage property
    fit_pdf_to_page: Optional[bool] = None
    # The input bin (tray) to use when printing. See the printer's capabilities for a list of supported input bins.
    input_bin: Optional[str] = None
    # The margin settings to use when printing.
    margin: Optional[print_margin.PrintMargin] = None
    # The media size to use when printing. Supports standard size names for ISO and ANSI media sizes.
    media_size: Optional[str] = None
    # The mediaType property
    media_type: Optional[str] = None
    # The multipageLayout property
    multipage_layout: Optional[print_multipage_layout.PrintMultipageLayout] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The orientation property
    orientation: Optional[print_orientation.PrintOrientation] = None
    # The outputBin property
    output_bin: Optional[str] = None
    # The pageRanges property
    page_ranges: Optional[List[integer_range.IntegerRange]] = None
    # The pagesPerSheet property
    pages_per_sheet: Optional[int] = None
    # The quality property
    quality: Optional[print_quality.PrintQuality] = None
    # The scaling property
    scaling: Optional[print_scaling.PrintScaling] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintJobConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintJobConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintJobConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import integer_range, printer_feed_orientation, print_color_mode, print_duplex_mode, print_finishing, print_margin, print_multipage_layout, print_orientation, print_quality, print_scaling

        fields: Dict[str, Callable[[Any], None]] = {
            "collate": lambda n : setattr(self, 'collate', n.get_bool_value()),
            "colorMode": lambda n : setattr(self, 'color_mode', n.get_enum_value(print_color_mode.PrintColorMode)),
            "copies": lambda n : setattr(self, 'copies', n.get_int_value()),
            "dpi": lambda n : setattr(self, 'dpi', n.get_int_value()),
            "duplexMode": lambda n : setattr(self, 'duplex_mode', n.get_enum_value(print_duplex_mode.PrintDuplexMode)),
            "feedOrientation": lambda n : setattr(self, 'feed_orientation', n.get_enum_value(printer_feed_orientation.PrinterFeedOrientation)),
            "finishings": lambda n : setattr(self, 'finishings', n.get_collection_of_enum_values(print_finishing.PrintFinishing)),
            "fitPdfToPage": lambda n : setattr(self, 'fit_pdf_to_page', n.get_bool_value()),
            "inputBin": lambda n : setattr(self, 'input_bin', n.get_str_value()),
            "margin": lambda n : setattr(self, 'margin', n.get_object_value(print_margin.PrintMargin)),
            "mediaSize": lambda n : setattr(self, 'media_size', n.get_str_value()),
            "mediaType": lambda n : setattr(self, 'media_type', n.get_str_value()),
            "multipageLayout": lambda n : setattr(self, 'multipage_layout', n.get_enum_value(print_multipage_layout.PrintMultipageLayout)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "orientation": lambda n : setattr(self, 'orientation', n.get_enum_value(print_orientation.PrintOrientation)),
            "outputBin": lambda n : setattr(self, 'output_bin', n.get_str_value()),
            "pagesPerSheet": lambda n : setattr(self, 'pages_per_sheet', n.get_int_value()),
            "pageRanges": lambda n : setattr(self, 'page_ranges', n.get_collection_of_object_values(integer_range.IntegerRange)),
            "quality": lambda n : setattr(self, 'quality', n.get_enum_value(print_quality.PrintQuality)),
            "scaling": lambda n : setattr(self, 'scaling', n.get_enum_value(print_scaling.PrintScaling)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("collate", self.collate)
        writer.write_enum_value("colorMode", self.color_mode)
        writer.write_int_value("copies", self.copies)
        writer.write_int_value("dpi", self.dpi)
        writer.write_enum_value("duplexMode", self.duplex_mode)
        writer.write_enum_value("feedOrientation", self.feed_orientation)
        writer.write_enum_value("finishings", self.finishings)
        writer.write_bool_value("fitPdfToPage", self.fit_pdf_to_page)
        writer.write_str_value("inputBin", self.input_bin)
        writer.write_object_value("margin", self.margin)
        writer.write_str_value("mediaSize", self.media_size)
        writer.write_str_value("mediaType", self.media_type)
        writer.write_enum_value("multipageLayout", self.multipage_layout)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("orientation", self.orientation)
        writer.write_str_value("outputBin", self.output_bin)
        writer.write_int_value("pagesPerSheet", self.pages_per_sheet)
        writer.write_collection_of_object_values("pageRanges", self.page_ranges)
        writer.write_enum_value("quality", self.quality)
        writer.write_enum_value("scaling", self.scaling)
        writer.write_additional_data_value(self.additional_data)
    

