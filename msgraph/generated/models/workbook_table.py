from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, workbook_table_column, workbook_table_row, workbook_table_sort, workbook_worksheet

from . import entity

@dataclass
class WorkbookTable(entity.Entity):
    # Represents a collection of all the columns in the table. Read-only.
    columns: Optional[List[workbook_table_column.WorkbookTableColumn]] = None
    # Indicates whether the first column contains special formatting.
    highlight_first_column: Optional[bool] = None
    # Indicates whether the last column contains special formatting.
    highlight_last_column: Optional[bool] = None
    # Legacy Id used in older Excle clients. The value of the identifier remains the same even when the table is renamed. This property should be interpreted as an opaque string value and should not be parsed to any other type. Read-only.
    legacy_id: Optional[str] = None
    # Name of the table.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a collection of all the rows in the table. Read-only.
    rows: Optional[List[workbook_table_row.WorkbookTableRow]] = None
    # Indicates whether the columns show banded formatting in which odd columns are highlighted differently from even ones to make reading the table easier.
    show_banded_columns: Optional[bool] = None
    # Indicates whether the rows show banded formatting in which odd rows are highlighted differently from even ones to make reading the table easier.
    show_banded_rows: Optional[bool] = None
    # Indicates whether the filter buttons are visible at the top of each column header. Setting this is only allowed if the table contains a header row.
    show_filter_button: Optional[bool] = None
    # Indicates whether the header row is visible or not. This value can be set to show or remove the header row.
    show_headers: Optional[bool] = None
    # Indicates whether the total row is visible or not. This value can be set to show or remove the total row.
    show_totals: Optional[bool] = None
    # Represents the sorting for the table. Read-only.
    sort: Optional[workbook_table_sort.WorkbookTableSort] = None
    # Constant value that represents the Table style. The possible values are: TableStyleLight1 thru TableStyleLight21, TableStyleMedium1 thru TableStyleMedium28, TableStyleStyleDark1 thru TableStyleStyleDark11. A custom user-defined style present in the workbook can also be specified.
    style: Optional[str] = None
    # The worksheet containing the current table. Read-only.
    worksheet: Optional[workbook_worksheet.WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookTable:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookTable
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookTable()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, workbook_table_column, workbook_table_row, workbook_table_sort, workbook_worksheet

        from . import entity, workbook_table_column, workbook_table_row, workbook_table_sort, workbook_worksheet

        fields: Dict[str, Callable[[Any], None]] = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(workbook_table_column.WorkbookTableColumn)),
            "highlightFirstColumn": lambda n : setattr(self, 'highlight_first_column', n.get_bool_value()),
            "highlightLastColumn": lambda n : setattr(self, 'highlight_last_column', n.get_bool_value()),
            "legacyId": lambda n : setattr(self, 'legacy_id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "rows": lambda n : setattr(self, 'rows', n.get_collection_of_object_values(workbook_table_row.WorkbookTableRow)),
            "showBandedColumns": lambda n : setattr(self, 'show_banded_columns', n.get_bool_value()),
            "showBandedRows": lambda n : setattr(self, 'show_banded_rows', n.get_bool_value()),
            "showFilterButton": lambda n : setattr(self, 'show_filter_button', n.get_bool_value()),
            "showHeaders": lambda n : setattr(self, 'show_headers', n.get_bool_value()),
            "showTotals": lambda n : setattr(self, 'show_totals', n.get_bool_value()),
            "sort": lambda n : setattr(self, 'sort', n.get_object_value(workbook_table_sort.WorkbookTableSort)),
            "style": lambda n : setattr(self, 'style', n.get_str_value()),
            "worksheet": lambda n : setattr(self, 'worksheet', n.get_object_value(workbook_worksheet.WorkbookWorksheet)),
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
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_bool_value("highlightFirstColumn", self.highlight_first_column)
        writer.write_bool_value("highlightLastColumn", self.highlight_last_column)
        writer.write_str_value("legacyId", self.legacy_id)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("rows", self.rows)
        writer.write_bool_value("showBandedColumns", self.show_banded_columns)
        writer.write_bool_value("showBandedRows", self.show_banded_rows)
        writer.write_bool_value("showFilterButton", self.show_filter_button)
        writer.write_bool_value("showHeaders", self.show_headers)
        writer.write_bool_value("showTotals", self.show_totals)
        writer.write_object_value("sort", self.sort)
        writer.write_str_value("style", self.style)
        writer.write_object_value("worksheet", self.worksheet)
    

