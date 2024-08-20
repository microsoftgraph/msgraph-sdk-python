from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat

from .entity import Entity

@dataclass
class WorkbookChartGridlines(Entity):
    # Represents the formatting of chart gridlines. Read-only.
    format: Optional[WorkbookChartGridlinesFormat] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the axis gridlines are visible.
    visible: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookChartGridlines:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartGridlines
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartGridlines()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat

        from .entity import Entity
        from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat

        fields: Dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(WorkbookChartGridlinesFormat)),
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
        writer.write_bool_value("visible", self.visible)
    

