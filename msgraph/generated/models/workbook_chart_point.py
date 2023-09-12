from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .json import Json
    from .workbook_chart_point_format import WorkbookChartPointFormat

from .entity import Entity

@dataclass
class WorkbookChartPoint(Entity):
    # Encapsulates the format properties chart point. Read-only.
    format: Optional[WorkbookChartPointFormat] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Returns the value of a chart point. Read-only.
    value: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartPoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartPoint
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartPoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .json import Json
        from .workbook_chart_point_format import WorkbookChartPointFormat

        from .entity import Entity
        from .json import Json
        from .workbook_chart_point_format import WorkbookChartPointFormat

        fields: Dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(WorkbookChartPointFormat)),
            "value": lambda n : setattr(self, 'value', n.get_object_value(Json)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("format", self.format)
        writer.write_object_value("value", self.value)
    

