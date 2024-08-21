from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_format_protection import WorkbookFormatProtection
    from .workbook_range_border import WorkbookRangeBorder
    from .workbook_range_fill import WorkbookRangeFill
    from .workbook_range_font import WorkbookRangeFont

from .entity import Entity

@dataclass
class WorkbookRangeFormat(Entity):
    # Collection of border objects that apply to the overall range selected Read-only.
    borders: Optional[List[WorkbookRangeBorder]] = None
    # The width of all columns within the range. If the column widths aren't uniform, null will be returned.
    column_width: Optional[float] = None
    # Returns the fill object defined on the overall range. Read-only.
    fill: Optional[WorkbookRangeFill] = None
    # Returns the font object defined on the overall range selected Read-only.
    font: Optional[WorkbookRangeFont] = None
    # The horizontal alignment for the specified object. Possible values are: General, Left, Center, Right, Fill, Justify, CenterAcrossSelection, Distributed.
    horizontal_alignment: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Returns the format protection object for a range. Read-only.
    protection: Optional[WorkbookFormatProtection] = None
    # The height of all rows in the range. If the row heights aren't uniform null will be returned.
    row_height: Optional[float] = None
    # The vertical alignment for the specified object. Possible values are: Top, Center, Bottom, Justify, Distributed.
    vertical_alignment: Optional[str] = None
    # Indicates whether Excel wraps the text in the object. A null value indicates that the entire range doesn't have a uniform wrap setting.
    wrap_text: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookRangeFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookRangeFormat
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookRangeFormat()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_format_protection import WorkbookFormatProtection
        from .workbook_range_border import WorkbookRangeBorder
        from .workbook_range_fill import WorkbookRangeFill
        from .workbook_range_font import WorkbookRangeFont

        from .entity import Entity
        from .workbook_format_protection import WorkbookFormatProtection
        from .workbook_range_border import WorkbookRangeBorder
        from .workbook_range_fill import WorkbookRangeFill
        from .workbook_range_font import WorkbookRangeFont

        fields: Dict[str, Callable[[Any], None]] = {
            "borders": lambda n : setattr(self, 'borders', n.get_collection_of_object_values(WorkbookRangeBorder)),
            "columnWidth": lambda n : setattr(self, 'column_width', n.get_float_value()),
            "fill": lambda n : setattr(self, 'fill', n.get_object_value(WorkbookRangeFill)),
            "font": lambda n : setattr(self, 'font', n.get_object_value(WorkbookRangeFont)),
            "horizontalAlignment": lambda n : setattr(self, 'horizontal_alignment', n.get_str_value()),
            "protection": lambda n : setattr(self, 'protection', n.get_object_value(WorkbookFormatProtection)),
            "rowHeight": lambda n : setattr(self, 'row_height', n.get_float_value()),
            "verticalAlignment": lambda n : setattr(self, 'vertical_alignment', n.get_str_value()),
            "wrapText": lambda n : setattr(self, 'wrap_text', n.get_bool_value()),
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
        writer.write_collection_of_object_values("borders", self.borders)
        writer.write_float_value("columnWidth", self.column_width)
        writer.write_object_value("fill", self.fill)
        writer.write_object_value("font", self.font)
        writer.write_str_value("horizontalAlignment", self.horizontal_alignment)
        writer.write_object_value("protection", self.protection)
        writer.write_float_value("rowHeight", self.row_height)
        writer.write_str_value("verticalAlignment", self.vertical_alignment)
        writer.write_bool_value("wrapText", self.wrap_text)
    

