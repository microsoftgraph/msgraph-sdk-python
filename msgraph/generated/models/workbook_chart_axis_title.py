from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat

from .entity import Entity

@dataclass
class WorkbookChartAxisTitle(Entity, Parsable):
    # Represents the formatting of chart axis title. Read-only.
    format: Optional[WorkbookChartAxisTitleFormat] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the axis title.
    text: Optional[str] = None
    # A Boolean that specifies the visibility of an axis title.
    visible: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookChartAxisTitle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartAxisTitle
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartAxisTitle()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat

        from .entity import Entity
        from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat

        fields: dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(WorkbookChartAxisTitleFormat)),
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
        writer.write_str_value("text", self.text)
        writer.write_bool_value("visible", self.visible)
    

