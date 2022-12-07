from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_format_protection = lazy_import('msgraph.generated.models.workbook_format_protection')
workbook_range_border = lazy_import('msgraph.generated.models.workbook_range_border')
workbook_range_fill = lazy_import('msgraph.generated.models.workbook_range_fill')
workbook_range_font = lazy_import('msgraph.generated.models.workbook_range_font')

class WorkbookRangeFormat(entity.Entity):
    @property
    def borders(self,) -> Optional[List[workbook_range_border.WorkbookRangeBorder]]:
        """
        Gets the borders property value. Collection of border objects that apply to the overall range selected Read-only.
        Returns: Optional[List[workbook_range_border.WorkbookRangeBorder]]
        """
        return self._borders
    
    @borders.setter
    def borders(self,value: Optional[List[workbook_range_border.WorkbookRangeBorder]] = None) -> None:
        """
        Sets the borders property value. Collection of border objects that apply to the overall range selected Read-only.
        Args:
            value: Value to set for the borders property.
        """
        self._borders = value
    
    @property
    def column_width(self,) -> Optional[float]:
        """
        Gets the columnWidth property value. Gets or sets the width of all colums within the range. If the column widths are not uniform, null will be returned.
        Returns: Optional[float]
        """
        return self._column_width
    
    @column_width.setter
    def column_width(self,value: Optional[float] = None) -> None:
        """
        Sets the columnWidth property value. Gets or sets the width of all colums within the range. If the column widths are not uniform, null will be returned.
        Args:
            value: Value to set for the columnWidth property.
        """
        self._column_width = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookRangeFormat and sets the default values.
        """
        super().__init__()
        # Collection of border objects that apply to the overall range selected Read-only.
        self._borders: Optional[List[workbook_range_border.WorkbookRangeBorder]] = None
        # Gets or sets the width of all colums within the range. If the column widths are not uniform, null will be returned.
        self._column_width: Optional[float] = None
        # Returns the fill object defined on the overall range. Read-only.
        self._fill: Optional[workbook_range_fill.WorkbookRangeFill] = None
        # Returns the font object defined on the overall range selected Read-only.
        self._font: Optional[workbook_range_font.WorkbookRangeFont] = None
        # Represents the horizontal alignment for the specified object. The possible values are: General, Left, Center, Right, Fill, Justify, CenterAcrossSelection, Distributed.
        self._horizontal_alignment: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Returns the format protection object for a range. Read-only.
        self._protection: Optional[workbook_format_protection.WorkbookFormatProtection] = None
        # Gets or sets the height of all rows in the range. If the row heights are not uniform null will be returned.
        self._row_height: Optional[float] = None
        # Represents the vertical alignment for the specified object. The possible values are: Top, Center, Bottom, Justify, Distributed.
        self._vertical_alignment: Optional[str] = None
        # Indicates if Excel wraps the text in the object. A null value indicates that the entire range doesn't have uniform wrap setting
        self._wrap_text: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookRangeFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookRangeFormat
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookRangeFormat()
    
    @property
    def fill(self,) -> Optional[workbook_range_fill.WorkbookRangeFill]:
        """
        Gets the fill property value. Returns the fill object defined on the overall range. Read-only.
        Returns: Optional[workbook_range_fill.WorkbookRangeFill]
        """
        return self._fill
    
    @fill.setter
    def fill(self,value: Optional[workbook_range_fill.WorkbookRangeFill] = None) -> None:
        """
        Sets the fill property value. Returns the fill object defined on the overall range. Read-only.
        Args:
            value: Value to set for the fill property.
        """
        self._fill = value
    
    @property
    def font(self,) -> Optional[workbook_range_font.WorkbookRangeFont]:
        """
        Gets the font property value. Returns the font object defined on the overall range selected Read-only.
        Returns: Optional[workbook_range_font.WorkbookRangeFont]
        """
        return self._font
    
    @font.setter
    def font(self,value: Optional[workbook_range_font.WorkbookRangeFont] = None) -> None:
        """
        Sets the font property value. Returns the font object defined on the overall range selected Read-only.
        Args:
            value: Value to set for the font property.
        """
        self._font = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "borders": lambda n : setattr(self, 'borders', n.get_collection_of_object_values(workbook_range_border.WorkbookRangeBorder)),
            "column_width": lambda n : setattr(self, 'column_width', n.get_float_value()),
            "fill": lambda n : setattr(self, 'fill', n.get_object_value(workbook_range_fill.WorkbookRangeFill)),
            "font": lambda n : setattr(self, 'font', n.get_object_value(workbook_range_font.WorkbookRangeFont)),
            "horizontal_alignment": lambda n : setattr(self, 'horizontal_alignment', n.get_str_value()),
            "protection": lambda n : setattr(self, 'protection', n.get_object_value(workbook_format_protection.WorkbookFormatProtection)),
            "row_height": lambda n : setattr(self, 'row_height', n.get_float_value()),
            "vertical_alignment": lambda n : setattr(self, 'vertical_alignment', n.get_str_value()),
            "wrap_text": lambda n : setattr(self, 'wrap_text', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def horizontal_alignment(self,) -> Optional[str]:
        """
        Gets the horizontalAlignment property value. Represents the horizontal alignment for the specified object. The possible values are: General, Left, Center, Right, Fill, Justify, CenterAcrossSelection, Distributed.
        Returns: Optional[str]
        """
        return self._horizontal_alignment
    
    @horizontal_alignment.setter
    def horizontal_alignment(self,value: Optional[str] = None) -> None:
        """
        Sets the horizontalAlignment property value. Represents the horizontal alignment for the specified object. The possible values are: General, Left, Center, Right, Fill, Justify, CenterAcrossSelection, Distributed.
        Args:
            value: Value to set for the horizontalAlignment property.
        """
        self._horizontal_alignment = value
    
    @property
    def protection(self,) -> Optional[workbook_format_protection.WorkbookFormatProtection]:
        """
        Gets the protection property value. Returns the format protection object for a range. Read-only.
        Returns: Optional[workbook_format_protection.WorkbookFormatProtection]
        """
        return self._protection
    
    @protection.setter
    def protection(self,value: Optional[workbook_format_protection.WorkbookFormatProtection] = None) -> None:
        """
        Sets the protection property value. Returns the format protection object for a range. Read-only.
        Args:
            value: Value to set for the protection property.
        """
        self._protection = value
    
    @property
    def row_height(self,) -> Optional[float]:
        """
        Gets the rowHeight property value. Gets or sets the height of all rows in the range. If the row heights are not uniform null will be returned.
        Returns: Optional[float]
        """
        return self._row_height
    
    @row_height.setter
    def row_height(self,value: Optional[float] = None) -> None:
        """
        Sets the rowHeight property value. Gets or sets the height of all rows in the range. If the row heights are not uniform null will be returned.
        Args:
            value: Value to set for the rowHeight property.
        """
        self._row_height = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("borders", self.borders)
        writer.write_float_value("columnWidth", self.column_width)
        writer.write_object_value("fill", self.fill)
        writer.write_object_value("font", self.font)
        writer.write_str_value("horizontalAlignment", self.horizontal_alignment)
        writer.write_object_value("protection", self.protection)
        writer.write_float_value("rowHeight", self.row_height)
        writer.write_str_value("verticalAlignment", self.vertical_alignment)
        writer.write_bool_value("wrapText", self.wrap_text)
    
    @property
    def vertical_alignment(self,) -> Optional[str]:
        """
        Gets the verticalAlignment property value. Represents the vertical alignment for the specified object. The possible values are: Top, Center, Bottom, Justify, Distributed.
        Returns: Optional[str]
        """
        return self._vertical_alignment
    
    @vertical_alignment.setter
    def vertical_alignment(self,value: Optional[str] = None) -> None:
        """
        Sets the verticalAlignment property value. Represents the vertical alignment for the specified object. The possible values are: Top, Center, Bottom, Justify, Distributed.
        Args:
            value: Value to set for the verticalAlignment property.
        """
        self._vertical_alignment = value
    
    @property
    def wrap_text(self,) -> Optional[bool]:
        """
        Gets the wrapText property value. Indicates if Excel wraps the text in the object. A null value indicates that the entire range doesn't have uniform wrap setting
        Returns: Optional[bool]
        """
        return self._wrap_text
    
    @wrap_text.setter
    def wrap_text(self,value: Optional[bool] = None) -> None:
        """
        Sets the wrapText property value. Indicates if Excel wraps the text in the object. A null value indicates that the entire range doesn't have uniform wrap setting
        Args:
            value: Value to set for the wrapText property.
        """
        self._wrap_text = value
    

