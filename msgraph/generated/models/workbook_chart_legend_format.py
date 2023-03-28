from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_chart_fill = lazy_import('msgraph.generated.models.workbook_chart_fill')
workbook_chart_font = lazy_import('msgraph.generated.models.workbook_chart_font')

class WorkbookChartLegendFormat(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new workbookChartLegendFormat and sets the default values.
        """
        super().__init__()
        # Represents the fill format of an object, which includes background formating information. Read-only.
        self._fill: Optional[workbook_chart_fill.WorkbookChartFill] = None
        # Represents the font attributes such as font name, font size, color, etc. of a chart legend. Read-only.
        self._font: Optional[workbook_chart_font.WorkbookChartFont] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartLegendFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartLegendFormat
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChartLegendFormat()
    
    @property
    def fill(self,) -> Optional[workbook_chart_fill.WorkbookChartFill]:
        """
        Gets the fill property value. Represents the fill format of an object, which includes background formating information. Read-only.
        Returns: Optional[workbook_chart_fill.WorkbookChartFill]
        """
        return self._fill
    
    @fill.setter
    def fill(self,value: Optional[workbook_chart_fill.WorkbookChartFill] = None) -> None:
        """
        Sets the fill property value. Represents the fill format of an object, which includes background formating information. Read-only.
        Args:
            value: Value to set for the fill property.
        """
        self._fill = value
    
    @property
    def font(self,) -> Optional[workbook_chart_font.WorkbookChartFont]:
        """
        Gets the font property value. Represents the font attributes such as font name, font size, color, etc. of a chart legend. Read-only.
        Returns: Optional[workbook_chart_font.WorkbookChartFont]
        """
        return self._font
    
    @font.setter
    def font(self,value: Optional[workbook_chart_font.WorkbookChartFont] = None) -> None:
        """
        Sets the font property value. Represents the font attributes such as font name, font size, color, etc. of a chart legend. Read-only.
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
    

