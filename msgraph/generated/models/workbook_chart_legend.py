from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart_legend_format import WorkbookChartLegendFormat

from .entity import Entity

@dataclass
class WorkbookChartLegend(Entity, Parsable):
    # Represents the formatting of a chart legend, which includes fill and font formatting. Read-only.
    format: Optional[WorkbookChartLegendFormat] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the chart legend should overlap with the main body of the chart.
    overlay: Optional[bool] = None
    # Represents the position of the legend on the chart. The possible values are: Top, Bottom, Left, Right, Corner, Custom.
    position: Optional[str] = None
    # Indicates whether the chart legend is visible.
    visible: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookChartLegend:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartLegend
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartLegend()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart_legend_format import WorkbookChartLegendFormat

        from .entity import Entity
        from .workbook_chart_legend_format import WorkbookChartLegendFormat

        fields: dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(WorkbookChartLegendFormat)),
            "overlay": lambda n : setattr(self, 'overlay', n.get_bool_value()),
            "position": lambda n : setattr(self, 'position', n.get_str_value()),
            "visible": lambda n : setattr(self, 'visible', n.get_bool_value()),
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
        writer.write_bool_value("overlay", self.overlay)
        writer.write_str_value("position", self.position)
        writer.write_bool_value("visible", self.visible)
    

