from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, workbook_chart, workbook_named_item, workbook_pivot_table, workbook_table, workbook_worksheet_protection

from . import entity

@dataclass
class WorkbookWorksheet(entity.Entity):
    # Returns collection of charts that are part of the worksheet. Read-only.
    charts: Optional[List[workbook_chart.WorkbookChart]] = None
    # The display name of the worksheet.
    name: Optional[str] = None
    # Returns collection of names that are associated with the worksheet. Read-only.
    names: Optional[List[workbook_named_item.WorkbookNamedItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of PivotTables that are part of the worksheet.
    pivot_tables: Optional[List[workbook_pivot_table.WorkbookPivotTable]] = None
    # The zero-based position of the worksheet within the workbook.
    position: Optional[int] = None
    # Returns sheet protection object for a worksheet. Read-only.
    protection: Optional[workbook_worksheet_protection.WorkbookWorksheetProtection] = None
    # Collection of tables that are part of the worksheet. Read-only.
    tables: Optional[List[workbook_table.WorkbookTable]] = None
    # The Visibility of the worksheet. The possible values are: Visible, Hidden, VeryHidden.
    visibility: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookWorksheet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookWorksheet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookWorksheet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, workbook_chart, workbook_named_item, workbook_pivot_table, workbook_table, workbook_worksheet_protection

        fields: Dict[str, Callable[[Any], None]] = {
            "charts": lambda n : setattr(self, 'charts', n.get_collection_of_object_values(workbook_chart.WorkbookChart)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "names": lambda n : setattr(self, 'names', n.get_collection_of_object_values(workbook_named_item.WorkbookNamedItem)),
            "pivotTables": lambda n : setattr(self, 'pivot_tables', n.get_collection_of_object_values(workbook_pivot_table.WorkbookPivotTable)),
            "position": lambda n : setattr(self, 'position', n.get_int_value()),
            "protection": lambda n : setattr(self, 'protection', n.get_object_value(workbook_worksheet_protection.WorkbookWorksheetProtection)),
            "tables": lambda n : setattr(self, 'tables', n.get_collection_of_object_values(workbook_table.WorkbookTable)),
            "visibility": lambda n : setattr(self, 'visibility', n.get_str_value()),
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
        writer.write_collection_of_object_values("charts", self.charts)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("names", self.names)
        writer.write_collection_of_object_values("pivotTables", self.pivot_tables)
        writer.write_int_value("position", self.position)
        writer.write_object_value("protection", self.protection)
        writer.write_collection_of_object_values("tables", self.tables)
        writer.write_str_value("visibility", self.visibility)
    

