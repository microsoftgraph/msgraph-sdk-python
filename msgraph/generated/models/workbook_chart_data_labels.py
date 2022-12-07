from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_chart_data_label_format = lazy_import('msgraph.generated.models.workbook_chart_data_label_format')

class WorkbookChartDataLabels(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new workbookChartDataLabels and sets the default values.
        """
        super().__init__()
        # Represents the format of chart data labels, which includes fill and font formatting. Read-only.
        self._format: Optional[workbook_chart_data_label_format.WorkbookChartDataLabelFormat] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # DataLabelPosition value that represents the position of the data label. The possible values are: None, Center, InsideEnd, InsideBase, OutsideEnd, Left, Right, Top, Bottom, BestFit, Callout.
        self._position: Optional[str] = None
        # String representing the separator used for the data labels on a chart.
        self._separator: Optional[str] = None
        # Boolean value representing if the data label bubble size is visible or not.
        self._show_bubble_size: Optional[bool] = None
        # Boolean value representing if the data label category name is visible or not.
        self._show_category_name: Optional[bool] = None
        # Boolean value representing if the data label legend key is visible or not.
        self._show_legend_key: Optional[bool] = None
        # Boolean value representing if the data label percentage is visible or not.
        self._show_percentage: Optional[bool] = None
        # Boolean value representing if the data label series name is visible or not.
        self._show_series_name: Optional[bool] = None
        # Boolean value representing if the data label value is visible or not.
        self._show_value: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartDataLabels:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartDataLabels
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChartDataLabels()
    
    @property
    def format(self,) -> Optional[workbook_chart_data_label_format.WorkbookChartDataLabelFormat]:
        """
        Gets the format property value. Represents the format of chart data labels, which includes fill and font formatting. Read-only.
        Returns: Optional[workbook_chart_data_label_format.WorkbookChartDataLabelFormat]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[workbook_chart_data_label_format.WorkbookChartDataLabelFormat] = None) -> None:
        """
        Sets the format property value. Represents the format of chart data labels, which includes fill and font formatting. Read-only.
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
            "format": lambda n : setattr(self, 'format', n.get_object_value(workbook_chart_data_label_format.WorkbookChartDataLabelFormat)),
            "position": lambda n : setattr(self, 'position', n.get_str_value()),
            "separator": lambda n : setattr(self, 'separator', n.get_str_value()),
            "show_bubble_size": lambda n : setattr(self, 'show_bubble_size', n.get_bool_value()),
            "show_category_name": lambda n : setattr(self, 'show_category_name', n.get_bool_value()),
            "show_legend_key": lambda n : setattr(self, 'show_legend_key', n.get_bool_value()),
            "show_percentage": lambda n : setattr(self, 'show_percentage', n.get_bool_value()),
            "show_series_name": lambda n : setattr(self, 'show_series_name', n.get_bool_value()),
            "show_value": lambda n : setattr(self, 'show_value', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def position(self,) -> Optional[str]:
        """
        Gets the position property value. DataLabelPosition value that represents the position of the data label. The possible values are: None, Center, InsideEnd, InsideBase, OutsideEnd, Left, Right, Top, Bottom, BestFit, Callout.
        Returns: Optional[str]
        """
        return self._position
    
    @position.setter
    def position(self,value: Optional[str] = None) -> None:
        """
        Sets the position property value. DataLabelPosition value that represents the position of the data label. The possible values are: None, Center, InsideEnd, InsideBase, OutsideEnd, Left, Right, Top, Bottom, BestFit, Callout.
        Args:
            value: Value to set for the position property.
        """
        self._position = value
    
    @property
    def separator(self,) -> Optional[str]:
        """
        Gets the separator property value. String representing the separator used for the data labels on a chart.
        Returns: Optional[str]
        """
        return self._separator
    
    @separator.setter
    def separator(self,value: Optional[str] = None) -> None:
        """
        Sets the separator property value. String representing the separator used for the data labels on a chart.
        Args:
            value: Value to set for the separator property.
        """
        self._separator = value
    
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
        writer.write_str_value("position", self.position)
        writer.write_str_value("separator", self.separator)
        writer.write_bool_value("showBubbleSize", self.show_bubble_size)
        writer.write_bool_value("showCategoryName", self.show_category_name)
        writer.write_bool_value("showLegendKey", self.show_legend_key)
        writer.write_bool_value("showPercentage", self.show_percentage)
        writer.write_bool_value("showSeriesName", self.show_series_name)
        writer.write_bool_value("showValue", self.show_value)
    
    @property
    def show_bubble_size(self,) -> Optional[bool]:
        """
        Gets the showBubbleSize property value. Boolean value representing if the data label bubble size is visible or not.
        Returns: Optional[bool]
        """
        return self._show_bubble_size
    
    @show_bubble_size.setter
    def show_bubble_size(self,value: Optional[bool] = None) -> None:
        """
        Sets the showBubbleSize property value. Boolean value representing if the data label bubble size is visible or not.
        Args:
            value: Value to set for the showBubbleSize property.
        """
        self._show_bubble_size = value
    
    @property
    def show_category_name(self,) -> Optional[bool]:
        """
        Gets the showCategoryName property value. Boolean value representing if the data label category name is visible or not.
        Returns: Optional[bool]
        """
        return self._show_category_name
    
    @show_category_name.setter
    def show_category_name(self,value: Optional[bool] = None) -> None:
        """
        Sets the showCategoryName property value. Boolean value representing if the data label category name is visible or not.
        Args:
            value: Value to set for the showCategoryName property.
        """
        self._show_category_name = value
    
    @property
    def show_legend_key(self,) -> Optional[bool]:
        """
        Gets the showLegendKey property value. Boolean value representing if the data label legend key is visible or not.
        Returns: Optional[bool]
        """
        return self._show_legend_key
    
    @show_legend_key.setter
    def show_legend_key(self,value: Optional[bool] = None) -> None:
        """
        Sets the showLegendKey property value. Boolean value representing if the data label legend key is visible or not.
        Args:
            value: Value to set for the showLegendKey property.
        """
        self._show_legend_key = value
    
    @property
    def show_percentage(self,) -> Optional[bool]:
        """
        Gets the showPercentage property value. Boolean value representing if the data label percentage is visible or not.
        Returns: Optional[bool]
        """
        return self._show_percentage
    
    @show_percentage.setter
    def show_percentage(self,value: Optional[bool] = None) -> None:
        """
        Sets the showPercentage property value. Boolean value representing if the data label percentage is visible or not.
        Args:
            value: Value to set for the showPercentage property.
        """
        self._show_percentage = value
    
    @property
    def show_series_name(self,) -> Optional[bool]:
        """
        Gets the showSeriesName property value. Boolean value representing if the data label series name is visible or not.
        Returns: Optional[bool]
        """
        return self._show_series_name
    
    @show_series_name.setter
    def show_series_name(self,value: Optional[bool] = None) -> None:
        """
        Sets the showSeriesName property value. Boolean value representing if the data label series name is visible or not.
        Args:
            value: Value to set for the showSeriesName property.
        """
        self._show_series_name = value
    
    @property
    def show_value(self,) -> Optional[bool]:
        """
        Gets the showValue property value. Boolean value representing if the data label value is visible or not.
        Returns: Optional[bool]
        """
        return self._show_value
    
    @show_value.setter
    def show_value(self,value: Optional[bool] = None) -> None:
        """
        Sets the showValue property value. Boolean value representing if the data label value is visible or not.
        Args:
            value: Value to set for the showValue property.
        """
        self._show_value = value
    

