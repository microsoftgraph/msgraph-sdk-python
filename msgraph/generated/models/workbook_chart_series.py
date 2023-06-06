from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, workbook_chart_point, workbook_chart_series_format

from . import entity

@dataclass
class WorkbookChartSeries(entity.Entity):
    # Represents the formatting of a chart series, which includes fill and line formatting. Read-only.
    format: Optional[workbook_chart_series_format.WorkbookChartSeriesFormat] = None
    # Represents the name of a series in a chart.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a collection of all points in the series. Read-only.
    points: Optional[List[workbook_chart_point.WorkbookChartPoint]] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, workbook_chart_point, workbook_chart_series_format

        fields: Dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(workbook_chart_series_format.WorkbookChartSeriesFormat)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "points": lambda n : setattr(self, 'points', n.get_collection_of_object_values(workbook_chart_point.WorkbookChartPoint)),
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
        writer.write_object_value("format", self.format)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("points", self.points)
    

