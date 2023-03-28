from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import integer_range, printer_feed_orientation, print_color_mode, print_duplex_mode, print_finishing, print_margin, print_multipage_layout, print_orientation, print_quality, print_scaling

class PrintJobConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new printJobConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Whether the printer should collate pages wehen printing multiple copies of a multi-page document.
        self._collate: Optional[bool] = None
        # The color mode the printer should use to print the job. Valid values are described in the table below. Read-only.
        self._color_mode: Optional[print_color_mode.PrintColorMode] = None
        # The number of copies that should be printed. Read-only.
        self._copies: Optional[int] = None
        # The resolution to use when printing the job, expressed in dots per inch (DPI). Read-only.
        self._dpi: Optional[int] = None
        # The duplex mode the printer should use when printing the job. Valid values are described in the table below. Read-only.
        self._duplex_mode: Optional[print_duplex_mode.PrintDuplexMode] = None
        # The orientation to use when feeding media into the printer. Valid values are described in the following table. Read-only.
        self._feed_orientation: Optional[printer_feed_orientation.PrinterFeedOrientation] = None
        # Finishing processes to use when printing.
        self._finishings: Optional[List[print_finishing.PrintFinishing]] = None
        # The fitPdfToPage property
        self._fit_pdf_to_page: Optional[bool] = None
        # The input bin (tray) to use when printing. See the printer's capabilities for a list of supported input bins.
        self._input_bin: Optional[str] = None
        # The margin settings to use when printing.
        self._margin: Optional[print_margin.PrintMargin] = None
        # The media size to use when printing. Supports standard size names for ISO and ANSI media sizes.
        self._media_size: Optional[str] = None
        # The mediaType property
        self._media_type: Optional[str] = None
        # The multipageLayout property
        self._multipage_layout: Optional[print_multipage_layout.PrintMultipageLayout] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The orientation property
        self._orientation: Optional[print_orientation.PrintOrientation] = None
        # The outputBin property
        self._output_bin: Optional[str] = None
        # The pageRanges property
        self._page_ranges: Optional[List[integer_range.IntegerRange]] = None
        # The pagesPerSheet property
        self._pages_per_sheet: Optional[int] = None
        # The quality property
        self._quality: Optional[print_quality.PrintQuality] = None
        # The scaling property
        self._scaling: Optional[print_scaling.PrintScaling] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def collate(self,) -> Optional[bool]:
        """
        Gets the collate property value. Whether the printer should collate pages wehen printing multiple copies of a multi-page document.
        Returns: Optional[bool]
        """
        return self._collate
    
    @collate.setter
    def collate(self,value: Optional[bool] = None) -> None:
        """
        Sets the collate property value. Whether the printer should collate pages wehen printing multiple copies of a multi-page document.
        Args:
            value: Value to set for the collate property.
        """
        self._collate = value
    
    @property
    def color_mode(self,) -> Optional[print_color_mode.PrintColorMode]:
        """
        Gets the colorMode property value. The color mode the printer should use to print the job. Valid values are described in the table below. Read-only.
        Returns: Optional[print_color_mode.PrintColorMode]
        """
        return self._color_mode
    
    @color_mode.setter
    def color_mode(self,value: Optional[print_color_mode.PrintColorMode] = None) -> None:
        """
        Sets the colorMode property value. The color mode the printer should use to print the job. Valid values are described in the table below. Read-only.
        Args:
            value: Value to set for the color_mode property.
        """
        self._color_mode = value
    
    @property
    def copies(self,) -> Optional[int]:
        """
        Gets the copies property value. The number of copies that should be printed. Read-only.
        Returns: Optional[int]
        """
        return self._copies
    
    @copies.setter
    def copies(self,value: Optional[int] = None) -> None:
        """
        Sets the copies property value. The number of copies that should be printed. Read-only.
        Args:
            value: Value to set for the copies property.
        """
        self._copies = value
    
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
    
    @property
    def dpi(self,) -> Optional[int]:
        """
        Gets the dpi property value. The resolution to use when printing the job, expressed in dots per inch (DPI). Read-only.
        Returns: Optional[int]
        """
        return self._dpi
    
    @dpi.setter
    def dpi(self,value: Optional[int] = None) -> None:
        """
        Sets the dpi property value. The resolution to use when printing the job, expressed in dots per inch (DPI). Read-only.
        Args:
            value: Value to set for the dpi property.
        """
        self._dpi = value
    
    @property
    def duplex_mode(self,) -> Optional[print_duplex_mode.PrintDuplexMode]:
        """
        Gets the duplexMode property value. The duplex mode the printer should use when printing the job. Valid values are described in the table below. Read-only.
        Returns: Optional[print_duplex_mode.PrintDuplexMode]
        """
        return self._duplex_mode
    
    @duplex_mode.setter
    def duplex_mode(self,value: Optional[print_duplex_mode.PrintDuplexMode] = None) -> None:
        """
        Sets the duplexMode property value. The duplex mode the printer should use when printing the job. Valid values are described in the table below. Read-only.
        Args:
            value: Value to set for the duplex_mode property.
        """
        self._duplex_mode = value
    
    @property
    def feed_orientation(self,) -> Optional[printer_feed_orientation.PrinterFeedOrientation]:
        """
        Gets the feedOrientation property value. The orientation to use when feeding media into the printer. Valid values are described in the following table. Read-only.
        Returns: Optional[printer_feed_orientation.PrinterFeedOrientation]
        """
        return self._feed_orientation
    
    @feed_orientation.setter
    def feed_orientation(self,value: Optional[printer_feed_orientation.PrinterFeedOrientation] = None) -> None:
        """
        Sets the feedOrientation property value. The orientation to use when feeding media into the printer. Valid values are described in the following table. Read-only.
        Args:
            value: Value to set for the feed_orientation property.
        """
        self._feed_orientation = value
    
    @property
    def finishings(self,) -> Optional[List[print_finishing.PrintFinishing]]:
        """
        Gets the finishings property value. Finishing processes to use when printing.
        Returns: Optional[List[print_finishing.PrintFinishing]]
        """
        return self._finishings
    
    @finishings.setter
    def finishings(self,value: Optional[List[print_finishing.PrintFinishing]] = None) -> None:
        """
        Sets the finishings property value. Finishing processes to use when printing.
        Args:
            value: Value to set for the finishings property.
        """
        self._finishings = value
    
    @property
    def fit_pdf_to_page(self,) -> Optional[bool]:
        """
        Gets the fitPdfToPage property value. The fitPdfToPage property
        Returns: Optional[bool]
        """
        return self._fit_pdf_to_page
    
    @fit_pdf_to_page.setter
    def fit_pdf_to_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the fitPdfToPage property value. The fitPdfToPage property
        Args:
            value: Value to set for the fit_pdf_to_page property.
        """
        self._fit_pdf_to_page = value
    
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
    
    @property
    def input_bin(self,) -> Optional[str]:
        """
        Gets the inputBin property value. The input bin (tray) to use when printing. See the printer's capabilities for a list of supported input bins.
        Returns: Optional[str]
        """
        return self._input_bin
    
    @input_bin.setter
    def input_bin(self,value: Optional[str] = None) -> None:
        """
        Sets the inputBin property value. The input bin (tray) to use when printing. See the printer's capabilities for a list of supported input bins.
        Args:
            value: Value to set for the input_bin property.
        """
        self._input_bin = value
    
    @property
    def margin(self,) -> Optional[print_margin.PrintMargin]:
        """
        Gets the margin property value. The margin settings to use when printing.
        Returns: Optional[print_margin.PrintMargin]
        """
        return self._margin
    
    @margin.setter
    def margin(self,value: Optional[print_margin.PrintMargin] = None) -> None:
        """
        Sets the margin property value. The margin settings to use when printing.
        Args:
            value: Value to set for the margin property.
        """
        self._margin = value
    
    @property
    def media_size(self,) -> Optional[str]:
        """
        Gets the mediaSize property value. The media size to use when printing. Supports standard size names for ISO and ANSI media sizes.
        Returns: Optional[str]
        """
        return self._media_size
    
    @media_size.setter
    def media_size(self,value: Optional[str] = None) -> None:
        """
        Sets the mediaSize property value. The media size to use when printing. Supports standard size names for ISO and ANSI media sizes.
        Args:
            value: Value to set for the media_size property.
        """
        self._media_size = value
    
    @property
    def media_type(self,) -> Optional[str]:
        """
        Gets the mediaType property value. The mediaType property
        Returns: Optional[str]
        """
        return self._media_type
    
    @media_type.setter
    def media_type(self,value: Optional[str] = None) -> None:
        """
        Sets the mediaType property value. The mediaType property
        Args:
            value: Value to set for the media_type property.
        """
        self._media_type = value
    
    @property
    def multipage_layout(self,) -> Optional[print_multipage_layout.PrintMultipageLayout]:
        """
        Gets the multipageLayout property value. The multipageLayout property
        Returns: Optional[print_multipage_layout.PrintMultipageLayout]
        """
        return self._multipage_layout
    
    @multipage_layout.setter
    def multipage_layout(self,value: Optional[print_multipage_layout.PrintMultipageLayout] = None) -> None:
        """
        Sets the multipageLayout property value. The multipageLayout property
        Args:
            value: Value to set for the multipage_layout property.
        """
        self._multipage_layout = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def orientation(self,) -> Optional[print_orientation.PrintOrientation]:
        """
        Gets the orientation property value. The orientation property
        Returns: Optional[print_orientation.PrintOrientation]
        """
        return self._orientation
    
    @orientation.setter
    def orientation(self,value: Optional[print_orientation.PrintOrientation] = None) -> None:
        """
        Sets the orientation property value. The orientation property
        Args:
            value: Value to set for the orientation property.
        """
        self._orientation = value
    
    @property
    def output_bin(self,) -> Optional[str]:
        """
        Gets the outputBin property value. The outputBin property
        Returns: Optional[str]
        """
        return self._output_bin
    
    @output_bin.setter
    def output_bin(self,value: Optional[str] = None) -> None:
        """
        Sets the outputBin property value. The outputBin property
        Args:
            value: Value to set for the output_bin property.
        """
        self._output_bin = value
    
    @property
    def page_ranges(self,) -> Optional[List[integer_range.IntegerRange]]:
        """
        Gets the pageRanges property value. The pageRanges property
        Returns: Optional[List[integer_range.IntegerRange]]
        """
        return self._page_ranges
    
    @page_ranges.setter
    def page_ranges(self,value: Optional[List[integer_range.IntegerRange]] = None) -> None:
        """
        Sets the pageRanges property value. The pageRanges property
        Args:
            value: Value to set for the page_ranges property.
        """
        self._page_ranges = value
    
    @property
    def pages_per_sheet(self,) -> Optional[int]:
        """
        Gets the pagesPerSheet property value. The pagesPerSheet property
        Returns: Optional[int]
        """
        return self._pages_per_sheet
    
    @pages_per_sheet.setter
    def pages_per_sheet(self,value: Optional[int] = None) -> None:
        """
        Sets the pagesPerSheet property value. The pagesPerSheet property
        Args:
            value: Value to set for the pages_per_sheet property.
        """
        self._pages_per_sheet = value
    
    @property
    def quality(self,) -> Optional[print_quality.PrintQuality]:
        """
        Gets the quality property value. The quality property
        Returns: Optional[print_quality.PrintQuality]
        """
        return self._quality
    
    @quality.setter
    def quality(self,value: Optional[print_quality.PrintQuality] = None) -> None:
        """
        Sets the quality property value. The quality property
        Args:
            value: Value to set for the quality property.
        """
        self._quality = value
    
    @property
    def scaling(self,) -> Optional[print_scaling.PrintScaling]:
        """
        Gets the scaling property value. The scaling property
        Returns: Optional[print_scaling.PrintScaling]
        """
        return self._scaling
    
    @scaling.setter
    def scaling(self,value: Optional[print_scaling.PrintScaling] = None) -> None:
        """
        Sets the scaling property value. The scaling property
        Args:
            value: Value to set for the scaling property.
        """
        self._scaling = value
    
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
    

