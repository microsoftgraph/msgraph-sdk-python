from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart_axis import WorkbookChartAxis

from .entity import Entity

@dataclass
class WorkbookChartAxes(Entity):
    # Represents the category axis in a chart. Read-only.
    category_axis: Optional[WorkbookChartAxis] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the series axis of a 3-dimensional chart. Read-only.
    series_axis: Optional[WorkbookChartAxis] = None
    # Represents the value axis in an axis. Read-only.
    value_axis: Optional[WorkbookChartAxis] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookChartAxes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartAxes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartAxes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart_axis import WorkbookChartAxis

        from .entity import Entity
        from .workbook_chart_axis import WorkbookChartAxis

        fields: Dict[str, Callable[[Any], None]] = {
            "categoryAxis": lambda n : setattr(self, 'category_axis', n.get_object_value(WorkbookChartAxis)),
            "seriesAxis": lambda n : setattr(self, 'series_axis', n.get_object_value(WorkbookChartAxis)),
            "valueAxis": lambda n : setattr(self, 'value_axis', n.get_object_value(WorkbookChartAxis)),
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
        writer.write_object_value("categoryAxis", self.category_axis)
        writer.write_object_value("seriesAxis", self.series_axis)
        writer.write_object_value("valueAxis", self.value_axis)
    

