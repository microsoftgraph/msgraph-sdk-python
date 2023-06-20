from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, workbook_chart_line_format

from . import entity

@dataclass
class WorkbookChartGridlinesFormat(entity.Entity):
    # Represents chart line formatting. Read-only.
    line: Optional[workbook_chart_line_format.WorkbookChartLineFormat] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartGridlinesFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartGridlinesFormat
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartGridlinesFormat()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, workbook_chart_line_format

        from . import entity, workbook_chart_line_format

        fields: Dict[str, Callable[[Any], None]] = {
            "line": lambda n : setattr(self, 'line', n.get_object_value(workbook_chart_line_format.WorkbookChartLineFormat)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("line", self.line)
    

