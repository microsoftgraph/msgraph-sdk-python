from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, workbook_chart_fill, workbook_chart_font

from . import entity

@dataclass
class WorkbookChartTitleFormat(entity.Entity):
    # Represents the fill format of an object, which includes background formatting information. Read-only.
    fill: Optional[workbook_chart_fill.WorkbookChartFill] = None
    # Represents the font attributes (font name, font size, color, etc.) for the current object. Read-only.
    font: Optional[workbook_chart_font.WorkbookChartFont] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartTitleFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartTitleFormat
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChartTitleFormat()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, workbook_chart_fill, workbook_chart_font

        fields: Dict[str, Callable[[Any], None]] = {
            "fill": lambda n : setattr(self, 'fill', n.get_object_value(workbook_chart_fill.WorkbookChartFill)),
            "font": lambda n : setattr(self, 'font', n.get_object_value(workbook_chart_font.WorkbookChartFont)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("fill", self.fill)
        writer.write_object_value("font", self.font)
    

