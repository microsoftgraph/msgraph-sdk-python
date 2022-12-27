from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_table_column = lazy_import('msgraph.generated.models.workbook_table_column')
workbook_table_row = lazy_import('msgraph.generated.models.workbook_table_row')
workbook_table_sort = lazy_import('msgraph.generated.models.workbook_table_sort')
workbook_worksheet = lazy_import('msgraph.generated.models.workbook_worksheet')

class WorkbookTable(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def columns(self,) -> Optional[List[workbook_table_column.WorkbookTableColumn]]:
        """
        Gets the columns property value. Represents a collection of all the columns in the table. Read-only.
        Returns: Optional[List[workbook_table_column.WorkbookTableColumn]]
        """
        return self._columns
    
    @columns.setter
    def columns(self,value: Optional[List[workbook_table_column.WorkbookTableColumn]] = None) -> None:
        """
        Sets the columns property value. Represents a collection of all the columns in the table. Read-only.
        Args:
            value: Value to set for the columns property.
        """
        self._columns = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookTable and sets the default values.
        """
        super().__init__()
        # Represents a collection of all the columns in the table. Read-only.
        self._columns: Optional[List[workbook_table_column.WorkbookTableColumn]] = None
        # Indicates whether the first column contains special formatting.
        self._highlight_first_column: Optional[bool] = None
        # Indicates whether the last column contains special formatting.
        self._highlight_last_column: Optional[bool] = None
        # Legacy Id used in older Excle clients. The value of the identifier remains the same even when the table is renamed. This property should be interpreted as an opaque string value and should not be parsed to any other type. Read-only.
        self._legacy_id: Optional[str] = None
        # Name of the table.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents a collection of all the rows in the table. Read-only.
        self._rows: Optional[List[workbook_table_row.WorkbookTableRow]] = None
        # Indicates whether the columns show banded formatting in which odd columns are highlighted differently from even ones to make reading the table easier.
        self._show_banded_columns: Optional[bool] = None
        # Indicates whether the rows show banded formatting in which odd rows are highlighted differently from even ones to make reading the table easier.
        self._show_banded_rows: Optional[bool] = None
        # Indicates whether the filter buttons are visible at the top of each column header. Setting this is only allowed if the table contains a header row.
        self._show_filter_button: Optional[bool] = None
        # Indicates whether the header row is visible or not. This value can be set to show or remove the header row.
        self._show_headers: Optional[bool] = None
        # Indicates whether the total row is visible or not. This value can be set to show or remove the total row.
        self._show_totals: Optional[bool] = None
        # Represents the sorting for the table. Read-only.
        self._sort: Optional[workbook_table_sort.WorkbookTableSort] = None
        # Constant value that represents the Table style. The possible values are: TableStyleLight1 thru TableStyleLight21, TableStyleMedium1 thru TableStyleMedium28, TableStyleStyleDark1 thru TableStyleStyleDark11. A custom user-defined style present in the workbook can also be specified.
        self._style: Optional[str] = None
        # The worksheet containing the current table. Read-only.
        self._worksheet: Optional[workbook_worksheet.WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookTable:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookTable
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookTable()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(workbook_table_column.WorkbookTableColumn)),
            "highlight_first_column": lambda n : setattr(self, 'highlight_first_column', n.get_bool_value()),
            "highlight_last_column": lambda n : setattr(self, 'highlight_last_column', n.get_bool_value()),
            "legacy_id": lambda n : setattr(self, 'legacy_id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "rows": lambda n : setattr(self, 'rows', n.get_collection_of_object_values(workbook_table_row.WorkbookTableRow)),
            "show_banded_columns": lambda n : setattr(self, 'show_banded_columns', n.get_bool_value()),
            "show_banded_rows": lambda n : setattr(self, 'show_banded_rows', n.get_bool_value()),
            "show_filter_button": lambda n : setattr(self, 'show_filter_button', n.get_bool_value()),
            "show_headers": lambda n : setattr(self, 'show_headers', n.get_bool_value()),
            "show_totals": lambda n : setattr(self, 'show_totals', n.get_bool_value()),
            "sort": lambda n : setattr(self, 'sort', n.get_object_value(workbook_table_sort.WorkbookTableSort)),
            "style": lambda n : setattr(self, 'style', n.get_str_value()),
            "worksheet": lambda n : setattr(self, 'worksheet', n.get_object_value(workbook_worksheet.WorkbookWorksheet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def highlight_first_column(self,) -> Optional[bool]:
        """
        Gets the highlightFirstColumn property value. Indicates whether the first column contains special formatting.
        Returns: Optional[bool]
        """
        return self._highlight_first_column
    
    @highlight_first_column.setter
    def highlight_first_column(self,value: Optional[bool] = None) -> None:
        """
        Sets the highlightFirstColumn property value. Indicates whether the first column contains special formatting.
        Args:
            value: Value to set for the highlightFirstColumn property.
        """
        self._highlight_first_column = value
    
    @property
    def highlight_last_column(self,) -> Optional[bool]:
        """
        Gets the highlightLastColumn property value. Indicates whether the last column contains special formatting.
        Returns: Optional[bool]
        """
        return self._highlight_last_column
    
    @highlight_last_column.setter
    def highlight_last_column(self,value: Optional[bool] = None) -> None:
        """
        Sets the highlightLastColumn property value. Indicates whether the last column contains special formatting.
        Args:
            value: Value to set for the highlightLastColumn property.
        """
        self._highlight_last_column = value
    
    @property
    def legacy_id(self,) -> Optional[str]:
        """
        Gets the legacyId property value. Legacy Id used in older Excle clients. The value of the identifier remains the same even when the table is renamed. This property should be interpreted as an opaque string value and should not be parsed to any other type. Read-only.
        Returns: Optional[str]
        """
        return self._legacy_id
    
    @legacy_id.setter
    def legacy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the legacyId property value. Legacy Id used in older Excle clients. The value of the identifier remains the same even when the table is renamed. This property should be interpreted as an opaque string value and should not be parsed to any other type. Read-only.
        Args:
            value: Value to set for the legacyId property.
        """
        self._legacy_id = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the table.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the table.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def rows(self,) -> Optional[List[workbook_table_row.WorkbookTableRow]]:
        """
        Gets the rows property value. Represents a collection of all the rows in the table. Read-only.
        Returns: Optional[List[workbook_table_row.WorkbookTableRow]]
        """
        return self._rows
    
    @rows.setter
    def rows(self,value: Optional[List[workbook_table_row.WorkbookTableRow]] = None) -> None:
        """
        Sets the rows property value. Represents a collection of all the rows in the table. Read-only.
        Args:
            value: Value to set for the rows property.
        """
        self._rows = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def show_banded_columns(self,) -> Optional[bool]:
        """
        Gets the showBandedColumns property value. Indicates whether the columns show banded formatting in which odd columns are highlighted differently from even ones to make reading the table easier.
        Returns: Optional[bool]
        """
        return self._show_banded_columns
    
    @show_banded_columns.setter
    def show_banded_columns(self,value: Optional[bool] = None) -> None:
        """
        Sets the showBandedColumns property value. Indicates whether the columns show banded formatting in which odd columns are highlighted differently from even ones to make reading the table easier.
        Args:
            value: Value to set for the showBandedColumns property.
        """
        self._show_banded_columns = value
    
    @property
    def show_banded_rows(self,) -> Optional[bool]:
        """
        Gets the showBandedRows property value. Indicates whether the rows show banded formatting in which odd rows are highlighted differently from even ones to make reading the table easier.
        Returns: Optional[bool]
        """
        return self._show_banded_rows
    
    @show_banded_rows.setter
    def show_banded_rows(self,value: Optional[bool] = None) -> None:
        """
        Sets the showBandedRows property value. Indicates whether the rows show banded formatting in which odd rows are highlighted differently from even ones to make reading the table easier.
        Args:
            value: Value to set for the showBandedRows property.
        """
        self._show_banded_rows = value
    
    @property
    def show_filter_button(self,) -> Optional[bool]:
        """
        Gets the showFilterButton property value. Indicates whether the filter buttons are visible at the top of each column header. Setting this is only allowed if the table contains a header row.
        Returns: Optional[bool]
        """
        return self._show_filter_button
    
    @show_filter_button.setter
    def show_filter_button(self,value: Optional[bool] = None) -> None:
        """
        Sets the showFilterButton property value. Indicates whether the filter buttons are visible at the top of each column header. Setting this is only allowed if the table contains a header row.
        Args:
            value: Value to set for the showFilterButton property.
        """
        self._show_filter_button = value
    
    @property
    def show_headers(self,) -> Optional[bool]:
        """
        Gets the showHeaders property value. Indicates whether the header row is visible or not. This value can be set to show or remove the header row.
        Returns: Optional[bool]
        """
        return self._show_headers
    
    @show_headers.setter
    def show_headers(self,value: Optional[bool] = None) -> None:
        """
        Sets the showHeaders property value. Indicates whether the header row is visible or not. This value can be set to show or remove the header row.
        Args:
            value: Value to set for the showHeaders property.
        """
        self._show_headers = value
    
    @property
    def show_totals(self,) -> Optional[bool]:
        """
        Gets the showTotals property value. Indicates whether the total row is visible or not. This value can be set to show or remove the total row.
        Returns: Optional[bool]
        """
        return self._show_totals
    
    @show_totals.setter
    def show_totals(self,value: Optional[bool] = None) -> None:
        """
        Sets the showTotals property value. Indicates whether the total row is visible or not. This value can be set to show or remove the total row.
        Args:
            value: Value to set for the showTotals property.
        """
        self._show_totals = value
    
    @property
    def sort(self,) -> Optional[workbook_table_sort.WorkbookTableSort]:
        """
        Gets the sort property value. Represents the sorting for the table. Read-only.
        Returns: Optional[workbook_table_sort.WorkbookTableSort]
        """
        return self._sort
    
    @sort.setter
    def sort(self,value: Optional[workbook_table_sort.WorkbookTableSort] = None) -> None:
        """
        Sets the sort property value. Represents the sorting for the table. Read-only.
        Args:
            value: Value to set for the sort property.
        """
        self._sort = value
    
    @property
    def style(self,) -> Optional[str]:
        """
        Gets the style property value. Constant value that represents the Table style. The possible values are: TableStyleLight1 thru TableStyleLight21, TableStyleMedium1 thru TableStyleMedium28, TableStyleStyleDark1 thru TableStyleStyleDark11. A custom user-defined style present in the workbook can also be specified.
        Returns: Optional[str]
        """
        return self._style
    
    @style.setter
    def style(self,value: Optional[str] = None) -> None:
        """
        Sets the style property value. Constant value that represents the Table style. The possible values are: TableStyleLight1 thru TableStyleLight21, TableStyleMedium1 thru TableStyleMedium28, TableStyleStyleDark1 thru TableStyleStyleDark11. A custom user-defined style present in the workbook can also be specified.
        Args:
            value: Value to set for the style property.
        """
        self._style = value
    
    @property
    def worksheet(self,) -> Optional[workbook_worksheet.WorkbookWorksheet]:
        """
        Gets the worksheet property value. The worksheet containing the current table. Read-only.
        Returns: Optional[workbook_worksheet.WorkbookWorksheet]
        """
        return self._worksheet
    
    @worksheet.setter
    def worksheet(self,value: Optional[workbook_worksheet.WorkbookWorksheet] = None) -> None:
        """
        Sets the worksheet property value. The worksheet containing the current table. Read-only.
        Args:
            value: Value to set for the worksheet property.
        """
        self._worksheet = value
    

