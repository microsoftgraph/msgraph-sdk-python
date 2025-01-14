from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_worksheet import WorkbookWorksheet

from .entity import Entity

@dataclass
class WorkbookPivotTable(Entity, Parsable):
    # The name of the pivot table.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The worksheet that contains the current pivot table. Read-only.
    worksheet: Optional[WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookPivotTable:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookPivotTable
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookPivotTable()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_worksheet import WorkbookWorksheet

        from .entity import Entity
        from .workbook_worksheet import WorkbookWorksheet

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "worksheet": lambda n : setattr(self, 'worksheet', n.get_object_value(WorkbookWorksheet)),
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
        writer.write_str_value("name", self.name)
        writer.write_object_value("worksheet", self.worksheet)
    

