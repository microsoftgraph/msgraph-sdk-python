from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, workbook_chart_axis

from . import entity

@dataclass
class WorkbookChartAxes(entity.Entity):
    # Represents the category axis in a chart. Read-only.
    category_axis: Optional[workbook_chart_axis.WorkbookChartAxis] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the series axis of a 3-dimensional chart. Read-only.
    series_axis: Optional[workbook_chart_axis.WorkbookChartAxis] = None
    # Represents the value axis in an axis. Read-only.
    value_axis: Optional[workbook_chart_axis.WorkbookChartAxis] = None
    
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
        from . import entity, workbook_chart_axis

        fields: Dict[str, Callable[[Any], None]] = {
            "categoryAxis": lambda n : setattr(self, 'category_axis', n.get_object_value(workbook_chart_axis.WorkbookChartAxis)),
            "seriesAxis": lambda n : setattr(self, 'series_axis', n.get_object_value(workbook_chart_axis.WorkbookChartAxis)),
            "valueAxis": lambda n : setattr(self, 'value_axis', n.get_object_value(workbook_chart_axis.WorkbookChartAxis)),
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
    

