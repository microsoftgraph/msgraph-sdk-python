from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart_title_format import WorkbookChartTitleFormat

from .entity import Entity

@dataclass
class WorkbookChartTitle(Entity):
    # The formatting of a chart title, which includes fill and font formatting. Read-only.
    format: Optional[WorkbookChartTitleFormat] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the chart title will overlay the chart or not.
    overlay: Optional[bool] = None
    # The title text of the chart.
    text: Optional[str] = None
    # Indicates whether the chart title is visible.
    visible: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookChartTitle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartTitle
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartTitle()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart_title_format import WorkbookChartTitleFormat

        from .entity import Entity
        from .workbook_chart_title_format import WorkbookChartTitleFormat

        fields: Dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(WorkbookChartTitleFormat)),
            "overlay": lambda n : setattr(self, 'overlay', n.get_bool_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_str_value("text", self.text)
        writer.write_bool_value("visible", self.visible)
    

