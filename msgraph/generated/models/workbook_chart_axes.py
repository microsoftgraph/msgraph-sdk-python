from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_chart_axis = lazy_import('msgraph.generated.models.workbook_chart_axis')

class WorkbookChartAxes(entity.Entity):
    @property
    def category_axis(self,) -> Optional[workbook_chart_axis.WorkbookChartAxis]:
        """
        Gets the categoryAxis property value. Represents the category axis in a chart. Read-only.
        Returns: Optional[workbook_chart_axis.WorkbookChartAxis]
        """
        return self._category_axis
    
    @category_axis.setter
    def category_axis(self,value: Optional[workbook_chart_axis.WorkbookChartAxis] = None) -> None:
        """
        Sets the categoryAxis property value. Represents the category axis in a chart. Read-only.
        Args:
            value: Value to set for the categoryAxis property.
        """
        self._category_axis = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookChartAxes and sets the default values.
        """
        super().__init__()
        # Represents the category axis in a chart. Read-only.
        self._category_axis: Optional[workbook_chart_axis.WorkbookChartAxis] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents the series axis of a 3-dimensional chart. Read-only.
        self._series_axis: Optional[workbook_chart_axis.WorkbookChartAxis] = None
        # Represents the value axis in an axis. Read-only.
        self._value_axis: Optional[workbook_chart_axis.WorkbookChartAxis] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartAxes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartAxes
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChartAxes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category_axis": lambda n : setattr(self, 'category_axis', n.get_object_value(workbook_chart_axis.WorkbookChartAxis)),
            "series_axis": lambda n : setattr(self, 'series_axis', n.get_object_value(workbook_chart_axis.WorkbookChartAxis)),
            "value_axis": lambda n : setattr(self, 'value_axis', n.get_object_value(workbook_chart_axis.WorkbookChartAxis)),
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
        writer.write_object_value("categoryAxis", self.category_axis)
        writer.write_object_value("seriesAxis", self.series_axis)
        writer.write_object_value("valueAxis", self.value_axis)
    
    @property
    def series_axis(self,) -> Optional[workbook_chart_axis.WorkbookChartAxis]:
        """
        Gets the seriesAxis property value. Represents the series axis of a 3-dimensional chart. Read-only.
        Returns: Optional[workbook_chart_axis.WorkbookChartAxis]
        """
        return self._series_axis
    
    @series_axis.setter
    def series_axis(self,value: Optional[workbook_chart_axis.WorkbookChartAxis] = None) -> None:
        """
        Sets the seriesAxis property value. Represents the series axis of a 3-dimensional chart. Read-only.
        Args:
            value: Value to set for the seriesAxis property.
        """
        self._series_axis = value
    
    @property
    def value_axis(self,) -> Optional[workbook_chart_axis.WorkbookChartAxis]:
        """
        Gets the valueAxis property value. Represents the value axis in an axis. Read-only.
        Returns: Optional[workbook_chart_axis.WorkbookChartAxis]
        """
        return self._value_axis
    
    @value_axis.setter
    def value_axis(self,value: Optional[workbook_chart_axis.WorkbookChartAxis] = None) -> None:
        """
        Sets the valueAxis property value. Represents the value axis in an axis. Read-only.
        Args:
            value: Value to set for the valueAxis property.
        """
        self._value_axis = value
    

