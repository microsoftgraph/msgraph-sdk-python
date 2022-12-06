from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
json = lazy_import('msgraph.generated.models.json')
workbook_chart_axis_format = lazy_import('msgraph.generated.models.workbook_chart_axis_format')
workbook_chart_axis_title = lazy_import('msgraph.generated.models.workbook_chart_axis_title')
workbook_chart_gridlines = lazy_import('msgraph.generated.models.workbook_chart_gridlines')

class WorkbookChartAxis(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new workbookChartAxis and sets the default values.
        """
        super().__init__()
        # Represents the formatting of a chart object, which includes line and font formatting. Read-only.
        self._format: Optional[workbook_chart_axis_format.WorkbookChartAxisFormat] = None
        # Returns a gridlines object that represents the major gridlines for the specified axis. Read-only.
        self._major_gridlines: Optional[workbook_chart_gridlines.WorkbookChartGridlines] = None
        # Represents the interval between two major tick marks. Can be set to a numeric value or an empty string.  The returned value is always a number.
        self._major_unit: Optional[json.Json] = None
        # Represents the maximum value on the value axis.  Can be set to a numeric value or an empty string (for automatic axis values).  The returned value is always a number.
        self._maximum: Optional[json.Json] = None
        # Represents the minimum value on the value axis. Can be set to a numeric value or an empty string (for automatic axis values).  The returned value is always a number.
        self._minimum: Optional[json.Json] = None
        # Returns a Gridlines object that represents the minor gridlines for the specified axis. Read-only.
        self._minor_gridlines: Optional[workbook_chart_gridlines.WorkbookChartGridlines] = None
        # Represents the interval between two minor tick marks. 'Can be set to a numeric value or an empty string (for automatic axis values). The returned value is always a number.
        self._minor_unit: Optional[json.Json] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents the axis title. Read-only.
        self._title: Optional[workbook_chart_axis_title.WorkbookChartAxisTitle] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartAxis:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartAxis
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChartAxis()
    
    @property
    def format(self,) -> Optional[workbook_chart_axis_format.WorkbookChartAxisFormat]:
        """
        Gets the format property value. Represents the formatting of a chart object, which includes line and font formatting. Read-only.
        Returns: Optional[workbook_chart_axis_format.WorkbookChartAxisFormat]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[workbook_chart_axis_format.WorkbookChartAxisFormat] = None) -> None:
        """
        Sets the format property value. Represents the formatting of a chart object, which includes line and font formatting. Read-only.
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
            "format": lambda n : setattr(self, 'format', n.get_object_value(workbook_chart_axis_format.WorkbookChartAxisFormat)),
            "major_gridlines": lambda n : setattr(self, 'major_gridlines', n.get_object_value(workbook_chart_gridlines.WorkbookChartGridlines)),
            "major_unit": lambda n : setattr(self, 'major_unit', n.get_object_value(json.Json)),
            "maximum": lambda n : setattr(self, 'maximum', n.get_object_value(json.Json)),
            "minimum": lambda n : setattr(self, 'minimum', n.get_object_value(json.Json)),
            "minor_gridlines": lambda n : setattr(self, 'minor_gridlines', n.get_object_value(workbook_chart_gridlines.WorkbookChartGridlines)),
            "minor_unit": lambda n : setattr(self, 'minor_unit', n.get_object_value(json.Json)),
            "title": lambda n : setattr(self, 'title', n.get_object_value(workbook_chart_axis_title.WorkbookChartAxisTitle)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def major_gridlines(self,) -> Optional[workbook_chart_gridlines.WorkbookChartGridlines]:
        """
        Gets the majorGridlines property value. Returns a gridlines object that represents the major gridlines for the specified axis. Read-only.
        Returns: Optional[workbook_chart_gridlines.WorkbookChartGridlines]
        """
        return self._major_gridlines
    
    @major_gridlines.setter
    def major_gridlines(self,value: Optional[workbook_chart_gridlines.WorkbookChartGridlines] = None) -> None:
        """
        Sets the majorGridlines property value. Returns a gridlines object that represents the major gridlines for the specified axis. Read-only.
        Args:
            value: Value to set for the majorGridlines property.
        """
        self._major_gridlines = value
    
    @property
    def major_unit(self,) -> Optional[json.Json]:
        """
        Gets the majorUnit property value. Represents the interval between two major tick marks. Can be set to a numeric value or an empty string.  The returned value is always a number.
        Returns: Optional[json.Json]
        """
        return self._major_unit
    
    @major_unit.setter
    def major_unit(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the majorUnit property value. Represents the interval between two major tick marks. Can be set to a numeric value or an empty string.  The returned value is always a number.
        Args:
            value: Value to set for the majorUnit property.
        """
        self._major_unit = value
    
    @property
    def maximum(self,) -> Optional[json.Json]:
        """
        Gets the maximum property value. Represents the maximum value on the value axis.  Can be set to a numeric value or an empty string (for automatic axis values).  The returned value is always a number.
        Returns: Optional[json.Json]
        """
        return self._maximum
    
    @maximum.setter
    def maximum(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the maximum property value. Represents the maximum value on the value axis.  Can be set to a numeric value or an empty string (for automatic axis values).  The returned value is always a number.
        Args:
            value: Value to set for the maximum property.
        """
        self._maximum = value
    
    @property
    def minimum(self,) -> Optional[json.Json]:
        """
        Gets the minimum property value. Represents the minimum value on the value axis. Can be set to a numeric value or an empty string (for automatic axis values).  The returned value is always a number.
        Returns: Optional[json.Json]
        """
        return self._minimum
    
    @minimum.setter
    def minimum(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the minimum property value. Represents the minimum value on the value axis. Can be set to a numeric value or an empty string (for automatic axis values).  The returned value is always a number.
        Args:
            value: Value to set for the minimum property.
        """
        self._minimum = value
    
    @property
    def minor_gridlines(self,) -> Optional[workbook_chart_gridlines.WorkbookChartGridlines]:
        """
        Gets the minorGridlines property value. Returns a Gridlines object that represents the minor gridlines for the specified axis. Read-only.
        Returns: Optional[workbook_chart_gridlines.WorkbookChartGridlines]
        """
        return self._minor_gridlines
    
    @minor_gridlines.setter
    def minor_gridlines(self,value: Optional[workbook_chart_gridlines.WorkbookChartGridlines] = None) -> None:
        """
        Sets the minorGridlines property value. Returns a Gridlines object that represents the minor gridlines for the specified axis. Read-only.
        Args:
            value: Value to set for the minorGridlines property.
        """
        self._minor_gridlines = value
    
    @property
    def minor_unit(self,) -> Optional[json.Json]:
        """
        Gets the minorUnit property value. Represents the interval between two minor tick marks. 'Can be set to a numeric value or an empty string (for automatic axis values). The returned value is always a number.
        Returns: Optional[json.Json]
        """
        return self._minor_unit
    
    @minor_unit.setter
    def minor_unit(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the minorUnit property value. Represents the interval between two minor tick marks. 'Can be set to a numeric value or an empty string (for automatic axis values). The returned value is always a number.
        Args:
            value: Value to set for the minorUnit property.
        """
        self._minor_unit = value
    
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
        writer.write_object_value("majorGridlines", self.major_gridlines)
        writer.write_object_value("majorUnit", self.major_unit)
        writer.write_object_value("maximum", self.maximum)
        writer.write_object_value("minimum", self.minimum)
        writer.write_object_value("minorGridlines", self.minor_gridlines)
        writer.write_object_value("minorUnit", self.minor_unit)
        writer.write_object_value("title", self.title)
    
    @property
    def title(self,) -> Optional[workbook_chart_axis_title.WorkbookChartAxisTitle]:
        """
        Gets the title property value. Represents the axis title. Read-only.
        Returns: Optional[workbook_chart_axis_title.WorkbookChartAxisTitle]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[workbook_chart_axis_title.WorkbookChartAxisTitle] = None) -> None:
        """
        Sets the title property value. Represents the axis title. Read-only.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

