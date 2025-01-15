from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart import WorkbookChart
    from .workbook_named_item import WorkbookNamedItem
    from .workbook_pivot_table import WorkbookPivotTable
    from .workbook_table import WorkbookTable
    from .workbook_worksheet_protection import WorkbookWorksheetProtection

from .entity import Entity

@dataclass
class WorkbookWorksheet(Entity, Parsable):
    # The list of charts that are part of the worksheet. Read-only.
    charts: Optional[list[WorkbookChart]] = None
    # The display name of the worksheet.
    name: Optional[str] = None
    # The list of names that are associated with the worksheet. Read-only.
    names: Optional[list[WorkbookNamedItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of piot tables that are part of the worksheet.
    pivot_tables: Optional[list[WorkbookPivotTable]] = None
    # The zero-based position of the worksheet within the workbook.
    position: Optional[int] = None
    # The sheet protection object for a worksheet. Read-only.
    protection: Optional[WorkbookWorksheetProtection] = None
    # The list of tables that are part of the worksheet. Read-only.
    tables: Optional[list[WorkbookTable]] = None
    # The visibility of the worksheet. The possible values are: Visible, Hidden, VeryHidden.
    visibility: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookWorksheet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookWorksheet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookWorksheet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart import WorkbookChart
        from .workbook_named_item import WorkbookNamedItem
        from .workbook_pivot_table import WorkbookPivotTable
        from .workbook_table import WorkbookTable
        from .workbook_worksheet_protection import WorkbookWorksheetProtection

        from .entity import Entity
        from .workbook_chart import WorkbookChart
        from .workbook_named_item import WorkbookNamedItem
        from .workbook_pivot_table import WorkbookPivotTable
        from .workbook_table import WorkbookTable
        from .workbook_worksheet_protection import WorkbookWorksheetProtection

        fields: dict[str, Callable[[Any], None]] = {
            "charts": lambda n : setattr(self, 'charts', n.get_collection_of_object_values(WorkbookChart)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "names": lambda n : setattr(self, 'names', n.get_collection_of_object_values(WorkbookNamedItem)),
            "pivotTables": lambda n : setattr(self, 'pivot_tables', n.get_collection_of_object_values(WorkbookPivotTable)),
            "position": lambda n : setattr(self, 'position', n.get_int_value()),
            "protection": lambda n : setattr(self, 'protection', n.get_object_value(WorkbookWorksheetProtection)),
            "tables": lambda n : setattr(self, 'tables', n.get_collection_of_object_values(WorkbookTable)),
            "visibility": lambda n : setattr(self, 'visibility', n.get_str_value()),
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
        writer.write_collection_of_object_values("charts", self.charts)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("names", self.names)
        writer.write_collection_of_object_values("pivotTables", self.pivot_tables)
        writer.write_int_value("position", self.position)
        writer.write_object_value("protection", self.protection)
        writer.write_collection_of_object_values("tables", self.tables)
        writer.write_str_value("visibility", self.visibility)
    

