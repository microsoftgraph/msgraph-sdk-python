from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .json import Json
    from .workbook_range_format import WorkbookRangeFormat
    from .workbook_range_sort import WorkbookRangeSort
    from .workbook_worksheet import WorkbookWorksheet

from .entity import Entity

@dataclass
class WorkbookRange(Entity):
    # Represents the range reference in A1-style. Address value contains the Sheet reference (for example, Sheet1!A1:B4). Read-only.
    address: Optional[str] = None
    # Represents range reference for the specified range in the language of the user. Read-only.
    address_local: Optional[str] = None
    # Number of cells in the range. Read-only.
    cell_count: Optional[int] = None
    # Represents the total number of columns in the range. Read-only.
    column_count: Optional[int] = None
    # Represents if all columns of the current range are hidden.
    column_hidden: Optional[bool] = None
    # Represents the column number of the first cell in the range. Zero-indexed. Read-only.
    column_index: Optional[int] = None
    # Returns a format object, encapsulating the range's font, fill, borders, alignment, and other properties. Read-only.
    format: Optional[WorkbookRangeFormat] = None
    # Represents the formula in A1-style notation.
    formulas: Optional[Json] = None
    # Represents the formula in A1-style notation, in the user's language and number-formatting locale.  For example, the English '=SUM(A1, 1.5)' formula would become '=SUMME(A1; 1,5)' in German.
    formulas_local: Optional[Json] = None
    # Represents the formula in R1C1-style notation.
    formulas_r1_c1: Optional[Json] = None
    # Represents if all cells of the current range are hidden. Read-only.
    hidden: Optional[bool] = None
    # Represents Excel's number format code for the given cell.
    number_format: Optional[Json] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Returns the total number of rows in the range. Read-only.
    row_count: Optional[int] = None
    # Represents if all rows of the current range are hidden.
    row_hidden: Optional[bool] = None
    # Returns the row number of the first cell in the range. Zero-indexed. Read-only.
    row_index: Optional[int] = None
    # The worksheet containing the current range. Read-only.
    sort: Optional[WorkbookRangeSort] = None
    # Text values of the specified range. The Text value doesn't depend on the cell width. The # sign substitution that happens in Excel UI doesn't affect the text value returned by the API. Read-only.
    text: Optional[Json] = None
    # Represents the type of data of each cell. The possible values are: Unknown, Empty, String, Integer, Double, Boolean, Error. Read-only.
    value_types: Optional[Json] = None
    # Represents the raw values of the specified range. The data returned could be of type string, number, or a boolean. Cell that contains an error returns the error string.
    values: Optional[Json] = None
    # The worksheet containing the current range. Read-only.
    worksheet: Optional[WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookRange
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookRange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .json import Json
        from .workbook_range_format import WorkbookRangeFormat
        from .workbook_range_sort import WorkbookRangeSort
        from .workbook_worksheet import WorkbookWorksheet

        from .entity import Entity
        from .json import Json
        from .workbook_range_format import WorkbookRangeFormat
        from .workbook_range_sort import WorkbookRangeSort
        from .workbook_worksheet import WorkbookWorksheet

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "addressLocal": lambda n : setattr(self, 'address_local', n.get_str_value()),
            "cellCount": lambda n : setattr(self, 'cell_count', n.get_int_value()),
            "columnCount": lambda n : setattr(self, 'column_count', n.get_int_value()),
            "columnHidden": lambda n : setattr(self, 'column_hidden', n.get_bool_value()),
            "columnIndex": lambda n : setattr(self, 'column_index', n.get_int_value()),
            "format": lambda n : setattr(self, 'format', n.get_object_value(WorkbookRangeFormat)),
            "formulas": lambda n : setattr(self, 'formulas', n.get_object_value(Json)),
            "formulasLocal": lambda n : setattr(self, 'formulas_local', n.get_object_value(Json)),
            "formulasR1C1": lambda n : setattr(self, 'formulas_r1_c1', n.get_object_value(Json)),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "numberFormat": lambda n : setattr(self, 'number_format', n.get_object_value(Json)),
            "rowCount": lambda n : setattr(self, 'row_count', n.get_int_value()),
            "rowHidden": lambda n : setattr(self, 'row_hidden', n.get_bool_value()),
            "rowIndex": lambda n : setattr(self, 'row_index', n.get_int_value()),
            "sort": lambda n : setattr(self, 'sort', n.get_object_value(WorkbookRangeSort)),
            "text": lambda n : setattr(self, 'text', n.get_object_value(Json)),
            "valueTypes": lambda n : setattr(self, 'value_types', n.get_object_value(Json)),
            "values": lambda n : setattr(self, 'values', n.get_object_value(Json)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("address", self.address)
        writer.write_str_value("addressLocal", self.address_local)
        writer.write_int_value("cellCount", self.cell_count)
        writer.write_int_value("columnCount", self.column_count)
        writer.write_bool_value("columnHidden", self.column_hidden)
        writer.write_int_value("columnIndex", self.column_index)
        writer.write_object_value("format", self.format)
        writer.write_object_value("formulas", self.formulas)
        writer.write_object_value("formulasLocal", self.formulas_local)
        writer.write_object_value("formulasR1C1", self.formulas_r1_c1)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_object_value("numberFormat", self.number_format)
        writer.write_int_value("rowCount", self.row_count)
        writer.write_bool_value("rowHidden", self.row_hidden)
        writer.write_int_value("rowIndex", self.row_index)
        writer.write_object_value("sort", self.sort)
        writer.write_object_value("text", self.text)
        writer.write_object_value("valueTypes", self.value_types)
        writer.write_object_value("values", self.values)
        writer.write_object_value("worksheet", self.worksheet)
    

