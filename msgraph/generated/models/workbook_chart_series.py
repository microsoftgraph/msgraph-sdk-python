from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_chart_point = lazy_import('msgraph.generated.models.workbook_chart_point')
workbook_chart_series_format = lazy_import('msgraph.generated.models.workbook_chart_series_format')

class WorkbookChartSeries(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new workbookChartSeries and sets the default values.
        """
        super().__init__()
        # Represents the formatting of a chart series, which includes fill and line formatting. Read-only.
        self._format: Optional[workbook_chart_series_format.WorkbookChartSeriesFormat] = None
        # Represents the name of a series in a chart.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents a collection of all points in the series. Read-only.
        self._points: Optional[List[workbook_chart_point.WorkbookChartPoint]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartSeries:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartSeries
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChartSeries()
    
    @property
    def format(self,) -> Optional[workbook_chart_series_format.WorkbookChartSeriesFormat]:
        """
        Gets the format property value. Represents the formatting of a chart series, which includes fill and line formatting. Read-only.
        Returns: Optional[workbook_chart_series_format.WorkbookChartSeriesFormat]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[workbook_chart_series_format.WorkbookChartSeriesFormat] = None) -> None:
        """
        Sets the format property value. Represents the formatting of a chart series, which includes fill and line formatting. Read-only.
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
            "format": lambda n : setattr(self, 'format', n.get_object_value(workbook_chart_series_format.WorkbookChartSeriesFormat)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "points": lambda n : setattr(self, 'points', n.get_collection_of_object_values(workbook_chart_point.WorkbookChartPoint)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Represents the name of a series in a chart.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Represents the name of a series in a chart.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def points(self,) -> Optional[List[workbook_chart_point.WorkbookChartPoint]]:
        """
        Gets the points property value. Represents a collection of all points in the series. Read-only.
        Returns: Optional[List[workbook_chart_point.WorkbookChartPoint]]
        """
        return self._points
    
    @points.setter
    def points(self,value: Optional[List[workbook_chart_point.WorkbookChartPoint]] = None) -> None:
        """
        Sets the points property value. Represents a collection of all points in the series. Read-only.
        Args:
            value: Value to set for the points property.
        """
        self._points = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("format", self.format)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("points", self.points)
    

