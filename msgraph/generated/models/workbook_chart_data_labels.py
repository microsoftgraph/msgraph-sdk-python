from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat

from .entity import Entity

@dataclass
class WorkbookChartDataLabels(Entity, Parsable):
    # Represents the format of chart data labels, which includes fill and font formatting. Read-only.
    format: Optional[WorkbookChartDataLabelFormat] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # DataLabelPosition value that represents the position of the data label. The possible values are: None, Center, InsideEnd, InsideBase, OutsideEnd, Left, Right, Top, Bottom, BestFit, Callout.
    position: Optional[str] = None
    # String that represents the separator used for the data labels on a chart.
    separator: Optional[str] = None
    # Boolean value that represents whether the data label bubble size is visible.
    show_bubble_size: Optional[bool] = None
    # Boolean value that represents whether the data label category name is visible.
    show_category_name: Optional[bool] = None
    # Boolean value that represents whether the data label legend key is visible.
    show_legend_key: Optional[bool] = None
    # Boolean value that represents whether the data label percentage is visible.
    show_percentage: Optional[bool] = None
    # Boolean value that represents whether the data label series name is visible.
    show_series_name: Optional[bool] = None
    # Boolean value that represents whether the data label value is visible.
    show_value: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookChartDataLabels:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartDataLabels
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartDataLabels()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat

        from .entity import Entity
        from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat

        fields: dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(WorkbookChartDataLabelFormat)),
            "position": lambda n : setattr(self, 'position', n.get_str_value()),
            "separator": lambda n : setattr(self, 'separator', n.get_str_value()),
            "showBubbleSize": lambda n : setattr(self, 'show_bubble_size', n.get_bool_value()),
            "showCategoryName": lambda n : setattr(self, 'show_category_name', n.get_bool_value()),
            "showLegendKey": lambda n : setattr(self, 'show_legend_key', n.get_bool_value()),
            "showPercentage": lambda n : setattr(self, 'show_percentage', n.get_bool_value()),
            "showSeriesName": lambda n : setattr(self, 'show_series_name', n.get_bool_value()),
            "showValue": lambda n : setattr(self, 'show_value', n.get_bool_value()),
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
        writer.write_str_value("position", self.position)
        writer.write_str_value("separator", self.separator)
        writer.write_bool_value("showBubbleSize", self.show_bubble_size)
        writer.write_bool_value("showCategoryName", self.show_category_name)
        writer.write_bool_value("showLegendKey", self.show_legend_key)
        writer.write_bool_value("showPercentage", self.show_percentage)
        writer.write_bool_value("showSeriesName", self.show_series_name)
        writer.write_bool_value("showValue", self.show_value)
    

