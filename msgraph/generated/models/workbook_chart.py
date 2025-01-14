from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart_area_format import WorkbookChartAreaFormat
    from .workbook_chart_axes import WorkbookChartAxes
    from .workbook_chart_data_labels import WorkbookChartDataLabels
    from .workbook_chart_legend import WorkbookChartLegend
    from .workbook_chart_series import WorkbookChartSeries
    from .workbook_chart_title import WorkbookChartTitle
    from .workbook_worksheet import WorkbookWorksheet

from .entity import Entity

@dataclass
class WorkbookChart(Entity, Parsable):
    # Represents chart axes. Read-only.
    axes: Optional[WorkbookChartAxes] = None
    # Represents the data labels on the chart. Read-only.
    data_labels: Optional[WorkbookChartDataLabels] = None
    # Encapsulates the format properties for the chart area. Read-only.
    format: Optional[WorkbookChartAreaFormat] = None
    # Represents the height, in points, of the chart object.
    height: Optional[float] = None
    # The distance, in points, from the left side of the chart to the worksheet origin.
    left: Optional[float] = None
    # Represents the legend for the chart. Read-only.
    legend: Optional[WorkbookChartLegend] = None
    # Represents the name of a chart object.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents either a single series or collection of series in the chart. Read-only.
    series: Optional[list[WorkbookChartSeries]] = None
    # Represents the title of the specified chart, including the text, visibility, position and formatting of the title. Read-only.
    title: Optional[WorkbookChartTitle] = None
    # Represents the distance, in points, from the top edge of the object to the top of row 1 (on a worksheet) or the top of the chart area (on a chart).
    top: Optional[float] = None
    # Represents the width, in points, of the chart object.
    width: Optional[float] = None
    # The worksheet containing the current chart. Read-only.
    worksheet: Optional[WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookChart:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChart
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChart()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart_area_format import WorkbookChartAreaFormat
        from .workbook_chart_axes import WorkbookChartAxes
        from .workbook_chart_data_labels import WorkbookChartDataLabels
        from .workbook_chart_legend import WorkbookChartLegend
        from .workbook_chart_series import WorkbookChartSeries
        from .workbook_chart_title import WorkbookChartTitle
        from .workbook_worksheet import WorkbookWorksheet

        from .entity import Entity
        from .workbook_chart_area_format import WorkbookChartAreaFormat
        from .workbook_chart_axes import WorkbookChartAxes
        from .workbook_chart_data_labels import WorkbookChartDataLabels
        from .workbook_chart_legend import WorkbookChartLegend
        from .workbook_chart_series import WorkbookChartSeries
        from .workbook_chart_title import WorkbookChartTitle
        from .workbook_worksheet import WorkbookWorksheet

        fields: dict[str, Callable[[Any], None]] = {
            "axes": lambda n : setattr(self, 'axes', n.get_object_value(WorkbookChartAxes)),
            "dataLabels": lambda n : setattr(self, 'data_labels', n.get_object_value(WorkbookChartDataLabels)),
            "format": lambda n : setattr(self, 'format', n.get_object_value(WorkbookChartAreaFormat)),
            "height": lambda n : setattr(self, 'height', n.get_float_value()),
            "left": lambda n : setattr(self, 'left', n.get_float_value()),
            "legend": lambda n : setattr(self, 'legend', n.get_object_value(WorkbookChartLegend)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "series": lambda n : setattr(self, 'series', n.get_collection_of_object_values(WorkbookChartSeries)),
            "title": lambda n : setattr(self, 'title', n.get_object_value(WorkbookChartTitle)),
            "top": lambda n : setattr(self, 'top', n.get_float_value()),
            "width": lambda n : setattr(self, 'width', n.get_float_value()),
            "worksheet": lambda n : setattr(self, 'worksheet', n.get_object_value(WorkbookWorksheet)),
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
        writer.write_object_value("axes", self.axes)
        writer.write_object_value("dataLabels", self.data_labels)
        writer.write_object_value("format", self.format)
        writer.write_float_value("height", self.height)
        writer.write_float_value("left", self.left)
        writer.write_object_value("legend", self.legend)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("series", self.series)
        writer.write_object_value("title", self.title)
        writer.write_float_value("top", self.top)
        writer.write_float_value("width", self.width)
        writer.write_object_value("worksheet", self.worksheet)
    

