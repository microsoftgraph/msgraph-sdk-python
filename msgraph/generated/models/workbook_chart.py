from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_chart_area_format = lazy_import('msgraph.generated.models.workbook_chart_area_format')
workbook_chart_axes = lazy_import('msgraph.generated.models.workbook_chart_axes')
workbook_chart_data_labels = lazy_import('msgraph.generated.models.workbook_chart_data_labels')
workbook_chart_legend = lazy_import('msgraph.generated.models.workbook_chart_legend')
workbook_chart_series = lazy_import('msgraph.generated.models.workbook_chart_series')
workbook_chart_title = lazy_import('msgraph.generated.models.workbook_chart_title')
workbook_worksheet = lazy_import('msgraph.generated.models.workbook_worksheet')

class WorkbookChart(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def axes(self,) -> Optional[workbook_chart_axes.WorkbookChartAxes]:
        """
        Gets the axes property value. Represents chart axes. Read-only.
        Returns: Optional[workbook_chart_axes.WorkbookChartAxes]
        """
        return self._axes
    
    @axes.setter
    def axes(self,value: Optional[workbook_chart_axes.WorkbookChartAxes] = None) -> None:
        """
        Sets the axes property value. Represents chart axes. Read-only.
        Args:
            value: Value to set for the axes property.
        """
        self._axes = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookChart and sets the default values.
        """
        super().__init__()
        # Represents chart axes. Read-only.
        self._axes: Optional[workbook_chart_axes.WorkbookChartAxes] = None
        # Represents the datalabels on the chart. Read-only.
        self._data_labels: Optional[workbook_chart_data_labels.WorkbookChartDataLabels] = None
        # Encapsulates the format properties for the chart area. Read-only.
        self._format: Optional[workbook_chart_area_format.WorkbookChartAreaFormat] = None
        # Represents the height, in points, of the chart object.
        self._height: Optional[float] = None
        # The distance, in points, from the left side of the chart to the worksheet origin.
        self._left: Optional[float] = None
        # Represents the legend for the chart. Read-only.
        self._legend: Optional[workbook_chart_legend.WorkbookChartLegend] = None
        # Represents the name of a chart object.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents either a single series or collection of series in the chart. Read-only.
        self._series: Optional[List[workbook_chart_series.WorkbookChartSeries]] = None
        # Represents the title of the specified chart, including the text, visibility, position and formating of the title. Read-only.
        self._title: Optional[workbook_chart_title.WorkbookChartTitle] = None
        # Represents the distance, in points, from the top edge of the object to the top of row 1 (on a worksheet) or the top of the chart area (on a chart).
        self._top: Optional[float] = None
        # Represents the width, in points, of the chart object.
        self._width: Optional[float] = None
        # The worksheet containing the current chart. Read-only.
        self._worksheet: Optional[workbook_worksheet.WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChart:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChart
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChart()
    
    @property
    def data_labels(self,) -> Optional[workbook_chart_data_labels.WorkbookChartDataLabels]:
        """
        Gets the dataLabels property value. Represents the datalabels on the chart. Read-only.
        Returns: Optional[workbook_chart_data_labels.WorkbookChartDataLabels]
        """
        return self._data_labels
    
    @data_labels.setter
    def data_labels(self,value: Optional[workbook_chart_data_labels.WorkbookChartDataLabels] = None) -> None:
        """
        Sets the dataLabels property value. Represents the datalabels on the chart. Read-only.
        Args:
            value: Value to set for the dataLabels property.
        """
        self._data_labels = value
    
    @property
    def format(self,) -> Optional[workbook_chart_area_format.WorkbookChartAreaFormat]:
        """
        Gets the format property value. Encapsulates the format properties for the chart area. Read-only.
        Returns: Optional[workbook_chart_area_format.WorkbookChartAreaFormat]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[workbook_chart_area_format.WorkbookChartAreaFormat] = None) -> None:
        """
        Sets the format property value. Encapsulates the format properties for the chart area. Read-only.
        Args:
            value: Value to set for the format property.
        """
        self._format = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "axes": lambda n : setattr(self, 'axes', n.get_object_value(workbook_chart_axes.WorkbookChartAxes)),
            "data_labels": lambda n : setattr(self, 'data_labels', n.get_object_value(workbook_chart_data_labels.WorkbookChartDataLabels)),
            "format": lambda n : setattr(self, 'format', n.get_object_value(workbook_chart_area_format.WorkbookChartAreaFormat)),
            "height": lambda n : setattr(self, 'height', n.get_float_value()),
            "left": lambda n : setattr(self, 'left', n.get_float_value()),
            "legend": lambda n : setattr(self, 'legend', n.get_object_value(workbook_chart_legend.WorkbookChartLegend)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "series": lambda n : setattr(self, 'series', n.get_collection_of_object_values(workbook_chart_series.WorkbookChartSeries)),
            "title": lambda n : setattr(self, 'title', n.get_object_value(workbook_chart_title.WorkbookChartTitle)),
            "top": lambda n : setattr(self, 'top', n.get_float_value()),
            "width": lambda n : setattr(self, 'width', n.get_float_value()),
            "worksheet": lambda n : setattr(self, 'worksheet', n.get_object_value(workbook_worksheet.WorkbookWorksheet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def height(self,) -> Optional[float]:
        """
        Gets the height property value. Represents the height, in points, of the chart object.
        Returns: Optional[float]
        """
        return self._height
    
    @height.setter
    def height(self,value: Optional[float] = None) -> None:
        """
        Sets the height property value. Represents the height, in points, of the chart object.
        Args:
            value: Value to set for the height property.
        """
        self._height = value
    
    @property
    def left(self,) -> Optional[float]:
        """
        Gets the left property value. The distance, in points, from the left side of the chart to the worksheet origin.
        Returns: Optional[float]
        """
        return self._left
    
    @left.setter
    def left(self,value: Optional[float] = None) -> None:
        """
        Sets the left property value. The distance, in points, from the left side of the chart to the worksheet origin.
        Args:
            value: Value to set for the left property.
        """
        self._left = value
    
    @property
    def legend(self,) -> Optional[workbook_chart_legend.WorkbookChartLegend]:
        """
        Gets the legend property value. Represents the legend for the chart. Read-only.
        Returns: Optional[workbook_chart_legend.WorkbookChartLegend]
        """
        return self._legend
    
    @legend.setter
    def legend(self,value: Optional[workbook_chart_legend.WorkbookChartLegend] = None) -> None:
        """
        Sets the legend property value. Represents the legend for the chart. Read-only.
        Args:
            value: Value to set for the legend property.
        """
        self._legend = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Represents the name of a chart object.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Represents the name of a chart object.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def series(self,) -> Optional[List[workbook_chart_series.WorkbookChartSeries]]:
        """
        Gets the series property value. Represents either a single series or collection of series in the chart. Read-only.
        Returns: Optional[List[workbook_chart_series.WorkbookChartSeries]]
        """
        return self._series
    
    @series.setter
    def series(self,value: Optional[List[workbook_chart_series.WorkbookChartSeries]] = None) -> None:
        """
        Sets the series property value. Represents either a single series or collection of series in the chart. Read-only.
        Args:
            value: Value to set for the series property.
        """
        self._series = value
    
    @property
    def title(self,) -> Optional[workbook_chart_title.WorkbookChartTitle]:
        """
        Gets the title property value. Represents the title of the specified chart, including the text, visibility, position and formating of the title. Read-only.
        Returns: Optional[workbook_chart_title.WorkbookChartTitle]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[workbook_chart_title.WorkbookChartTitle] = None) -> None:
        """
        Sets the title property value. Represents the title of the specified chart, including the text, visibility, position and formating of the title. Read-only.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def top(self,) -> Optional[float]:
        """
        Gets the top property value. Represents the distance, in points, from the top edge of the object to the top of row 1 (on a worksheet) or the top of the chart area (on a chart).
        Returns: Optional[float]
        """
        return self._top
    
    @top.setter
    def top(self,value: Optional[float] = None) -> None:
        """
        Sets the top property value. Represents the distance, in points, from the top edge of the object to the top of row 1 (on a worksheet) or the top of the chart area (on a chart).
        Args:
            value: Value to set for the top property.
        """
        self._top = value
    
    @property
    def width(self,) -> Optional[float]:
        """
        Gets the width property value. Represents the width, in points, of the chart object.
        Returns: Optional[float]
        """
        return self._width
    
    @width.setter
    def width(self,value: Optional[float] = None) -> None:
        """
        Sets the width property value. Represents the width, in points, of the chart object.
        Args:
            value: Value to set for the width property.
        """
        self._width = value
    
    @property
    def worksheet(self,) -> Optional[workbook_worksheet.WorkbookWorksheet]:
        """
        Gets the worksheet property value. The worksheet containing the current chart. Read-only.
        Returns: Optional[workbook_worksheet.WorkbookWorksheet]
        """
        return self._worksheet
    
    @worksheet.setter
    def worksheet(self,value: Optional[workbook_worksheet.WorkbookWorksheet] = None) -> None:
        """
        Sets the worksheet property value. The worksheet containing the current chart. Read-only.
        Args:
            value: Value to set for the worksheet property.
        """
        self._worksheet = value
    

