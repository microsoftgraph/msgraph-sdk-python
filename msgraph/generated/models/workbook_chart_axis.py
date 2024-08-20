from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart_axis_format import WorkbookChartAxisFormat
    from .workbook_chart_axis_title import WorkbookChartAxisTitle
    from .workbook_chart_gridlines import WorkbookChartGridlines

from .entity import Entity

@dataclass
class WorkbookChartAxis(Entity):
    # Represents the formatting of a chart object, which includes line and font formatting. Read-only.
    format: Optional[WorkbookChartAxisFormat] = None
    # Returns a gridlines object that represents the major gridlines for the specified axis. Read-only.
    major_gridlines: Optional[WorkbookChartGridlines] = None
    # Returns a Gridlines object that represents the minor gridlines for the specified axis. Read-only.
    minor_gridlines: Optional[WorkbookChartGridlines] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the axis title. Read-only.
    title: Optional[WorkbookChartAxisTitle] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookChartAxis:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartAxis
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartAxis()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart_axis_format import WorkbookChartAxisFormat
        from .workbook_chart_axis_title import WorkbookChartAxisTitle
        from .workbook_chart_gridlines import WorkbookChartGridlines

        from .entity import Entity
        from .workbook_chart_axis_format import WorkbookChartAxisFormat
        from .workbook_chart_axis_title import WorkbookChartAxisTitle
        from .workbook_chart_gridlines import WorkbookChartGridlines

        fields: Dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(WorkbookChartAxisFormat)),
            "majorGridlines": lambda n : setattr(self, 'major_gridlines', n.get_object_value(WorkbookChartGridlines)),
            "minorGridlines": lambda n : setattr(self, 'minor_gridlines', n.get_object_value(WorkbookChartGridlines)),
            "title": lambda n : setattr(self, 'title', n.get_object_value(WorkbookChartAxisTitle)),
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
        writer.write_object_value("format", self.format)
        writer.write_object_value("majorGridlines", self.major_gridlines)
        writer.write_object_value("minorGridlines", self.minor_gridlines)
        writer.write_object_value("title", self.title)
    

