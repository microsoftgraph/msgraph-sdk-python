from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
json = lazy_import('msgraph.generated.models.json')
workbook_range_format = lazy_import('msgraph.generated.models.workbook_range_format')
workbook_range_sort = lazy_import('msgraph.generated.models.workbook_range_sort')
workbook_worksheet = lazy_import('msgraph.generated.models.workbook_worksheet')

class WorkbookRange(entity.Entity):
    @property
    def address(self,) -> Optional[str]:
        """
        Gets the address property value. Represents the range reference in A1-style. Address value will contain the Sheet reference (e.g. Sheet1!A1:B4). Read-only.
        Returns: Optional[str]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[str] = None) -> None:
        """
        Sets the address property value. Represents the range reference in A1-style. Address value will contain the Sheet reference (e.g. Sheet1!A1:B4). Read-only.
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    @property
    def address_local(self,) -> Optional[str]:
        """
        Gets the addressLocal property value. Represents range reference for the specified range in the language of the user. Read-only.
        Returns: Optional[str]
        """
        return self._address_local
    
    @address_local.setter
    def address_local(self,value: Optional[str] = None) -> None:
        """
        Sets the addressLocal property value. Represents range reference for the specified range in the language of the user. Read-only.
        Args:
            value: Value to set for the addressLocal property.
        """
        self._address_local = value
    
    @property
    def cell_count(self,) -> Optional[int]:
        """
        Gets the cellCount property value. Number of cells in the range. Read-only.
        Returns: Optional[int]
        """
        return self._cell_count
    
    @cell_count.setter
    def cell_count(self,value: Optional[int] = None) -> None:
        """
        Sets the cellCount property value. Number of cells in the range. Read-only.
        Args:
            value: Value to set for the cellCount property.
        """
        self._cell_count = value
    
    @property
    def column_count(self,) -> Optional[int]:
        """
        Gets the columnCount property value. Represents the total number of columns in the range. Read-only.
        Returns: Optional[int]
        """
        return self._column_count
    
    @column_count.setter
    def column_count(self,value: Optional[int] = None) -> None:
        """
        Sets the columnCount property value. Represents the total number of columns in the range. Read-only.
        Args:
            value: Value to set for the columnCount property.
        """
        self._column_count = value
    
    @property
    def column_hidden(self,) -> Optional[bool]:
        """
        Gets the columnHidden property value. Represents if all columns of the current range are hidden.
        Returns: Optional[bool]
        """
        return self._column_hidden
    
    @column_hidden.setter
    def column_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the columnHidden property value. Represents if all columns of the current range are hidden.
        Args:
            value: Value to set for the columnHidden property.
        """
        self._column_hidden = value
    
    @property
    def column_index(self,) -> Optional[int]:
        """
        Gets the columnIndex property value. Represents the column number of the first cell in the range. Zero-indexed. Read-only.
        Returns: Optional[int]
        """
        return self._column_index
    
    @column_index.setter
    def column_index(self,value: Optional[int] = None) -> None:
        """
        Sets the columnIndex property value. Represents the column number of the first cell in the range. Zero-indexed. Read-only.
        Args:
            value: Value to set for the columnIndex property.
        """
        self._column_index = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WorkbookRange and sets the default values.
        """
        super().__init__()
        # Represents the range reference in A1-style. Address value will contain the Sheet reference (e.g. Sheet1!A1:B4). Read-only.
        self._address: Optional[str] = None
        # Represents range reference for the specified range in the language of the user. Read-only.
        self._address_local: Optional[str] = None
        # Number of cells in the range. Read-only.
        self._cell_count: Optional[int] = None
        # Represents the total number of columns in the range. Read-only.
        self._column_count: Optional[int] = None
        # Represents if all columns of the current range are hidden.
        self._column_hidden: Optional[bool] = None
        # Represents the column number of the first cell in the range. Zero-indexed. Read-only.
        self._column_index: Optional[int] = None
        # Returns a format object, encapsulating the range's font, fill, borders, alignment, and other properties. Read-only.
        self._format: Optional[workbook_range_format.WorkbookRangeFormat] = None
        # Represents the formula in A1-style notation.
        self._formulas: Optional[json.Json] = None
        # Represents the formula in A1-style notation, in the user's language and number-formatting locale.  For example, the English '=SUM(A1, 1.5)' formula would become '=SUMME(A1; 1,5)' in German.
        self._formulas_local: Optional[json.Json] = None
        # Represents the formula in R1C1-style notation.
        self._formulas_r1_c1: Optional[json.Json] = None
        # Represents if all cells of the current range are hidden. Read-only.
        self._hidden: Optional[bool] = None
        # Represents Excel's number format code for the given cell.
        self._number_format: Optional[json.Json] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Returns the total number of rows in the range. Read-only.
        self._row_count: Optional[int] = None
        # Represents if all rows of the current range are hidden.
        self._row_hidden: Optional[bool] = None
        # Returns the row number of the first cell in the range. Zero-indexed. Read-only.
        self._row_index: Optional[int] = None
        # The worksheet containing the current range. Read-only.
        self._sort: Optional[workbook_range_sort.WorkbookRangeSort] = None
        # Text values of the specified range. The Text value will not depend on the cell width. The # sign substitution that happens in Excel UI will not affect the text value returned by the API. Read-only.
        self._text: Optional[json.Json] = None
        # Represents the raw values of the specified range. The data returned could be of type string, number, or a boolean. Cell that contain an error will return the error string.
        self._values: Optional[json.Json] = None
        # Represents the type of data of each cell. The possible values are: Unknown, Empty, String, Integer, Double, Boolean, Error. Read-only.
        self._value_types: Optional[json.Json] = None
        # The worksheet containing the current range. Read-only.
        self._worksheet: Optional[workbook_worksheet.WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookRange
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookRange()
    
    @property
    def format(self,) -> Optional[workbook_range_format.WorkbookRangeFormat]:
        """
        Gets the format property value. Returns a format object, encapsulating the range's font, fill, borders, alignment, and other properties. Read-only.
        Returns: Optional[workbook_range_format.WorkbookRangeFormat]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[workbook_range_format.WorkbookRangeFormat] = None) -> None:
        """
        Sets the format property value. Returns a format object, encapsulating the range's font, fill, borders, alignment, and other properties. Read-only.
        Args:
            value: Value to set for the format property.
        """
        self._format = value
    
    @property
    def formulas(self,) -> Optional[json.Json]:
        """
        Gets the formulas property value. Represents the formula in A1-style notation.
        Returns: Optional[json.Json]
        """
        return self._formulas
    
    @formulas.setter
    def formulas(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the formulas property value. Represents the formula in A1-style notation.
        Args:
            value: Value to set for the formulas property.
        """
        self._formulas = value
    
    @property
    def formulas_local(self,) -> Optional[json.Json]:
        """
        Gets the formulasLocal property value. Represents the formula in A1-style notation, in the user's language and number-formatting locale.  For example, the English '=SUM(A1, 1.5)' formula would become '=SUMME(A1; 1,5)' in German.
        Returns: Optional[json.Json]
        """
        return self._formulas_local
    
    @formulas_local.setter
    def formulas_local(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the formulasLocal property value. Represents the formula in A1-style notation, in the user's language and number-formatting locale.  For example, the English '=SUM(A1, 1.5)' formula would become '=SUMME(A1; 1,5)' in German.
        Args:
            value: Value to set for the formulasLocal property.
        """
        self._formulas_local = value
    
    @property
    def formulas_r1_c1(self,) -> Optional[json.Json]:
        """
        Gets the formulasR1C1 property value. Represents the formula in R1C1-style notation.
        Returns: Optional[json.Json]
        """
        return self._formulas_r1_c1
    
    @formulas_r1_c1.setter
    def formulas_r1_c1(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the formulasR1C1 property value. Represents the formula in R1C1-style notation.
        Args:
            value: Value to set for the formulasR1C1 property.
        """
        self._formulas_r1_c1 = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "address_local": lambda n : setattr(self, 'address_local', n.get_str_value()),
            "cell_count": lambda n : setattr(self, 'cell_count', n.get_int_value()),
            "column_count": lambda n : setattr(self, 'column_count', n.get_int_value()),
            "column_hidden": lambda n : setattr(self, 'column_hidden', n.get_bool_value()),
            "column_index": lambda n : setattr(self, 'column_index', n.get_int_value()),
            "format": lambda n : setattr(self, 'format', n.get_object_value(workbook_range_format.WorkbookRangeFormat)),
            "formulas": lambda n : setattr(self, 'formulas', n.get_object_value(json.Json)),
            "formulas_local": lambda n : setattr(self, 'formulas_local', n.get_object_value(json.Json)),
            "formulas_r1_c1": lambda n : setattr(self, 'formulas_r1_c1', n.get_object_value(json.Json)),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "number_format": lambda n : setattr(self, 'number_format', n.get_object_value(json.Json)),
            "row_count": lambda n : setattr(self, 'row_count', n.get_int_value()),
            "row_hidden": lambda n : setattr(self, 'row_hidden', n.get_bool_value()),
            "row_index": lambda n : setattr(self, 'row_index', n.get_int_value()),
            "sort": lambda n : setattr(self, 'sort', n.get_object_value(workbook_range_sort.WorkbookRangeSort)),
            "text": lambda n : setattr(self, 'text', n.get_object_value(json.Json)),
            "values": lambda n : setattr(self, 'values', n.get_object_value(json.Json)),
            "value_types": lambda n : setattr(self, 'value_types', n.get_object_value(json.Json)),
            "worksheet": lambda n : setattr(self, 'worksheet', n.get_object_value(workbook_worksheet.WorkbookWorksheet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hidden(self,) -> Optional[bool]:
        """
        Gets the hidden property value. Represents if all cells of the current range are hidden. Read-only.
        Returns: Optional[bool]
        """
        return self._hidden
    
    @hidden.setter
    def hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the hidden property value. Represents if all cells of the current range are hidden. Read-only.
        Args:
            value: Value to set for the hidden property.
        """
        self._hidden = value
    
    @property
    def number_format(self,) -> Optional[json.Json]:
        """
        Gets the numberFormat property value. Represents Excel's number format code for the given cell.
        Returns: Optional[json.Json]
        """
        return self._number_format
    
    @number_format.setter
    def number_format(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the numberFormat property value. Represents Excel's number format code for the given cell.
        Args:
            value: Value to set for the numberFormat property.
        """
        self._number_format = value
    
    @property
    def row_count(self,) -> Optional[int]:
        """
        Gets the rowCount property value. Returns the total number of rows in the range. Read-only.
        Returns: Optional[int]
        """
        return self._row_count
    
    @row_count.setter
    def row_count(self,value: Optional[int] = None) -> None:
        """
        Sets the rowCount property value. Returns the total number of rows in the range. Read-only.
        Args:
            value: Value to set for the rowCount property.
        """
        self._row_count = value
    
    @property
    def row_hidden(self,) -> Optional[bool]:
        """
        Gets the rowHidden property value. Represents if all rows of the current range are hidden.
        Returns: Optional[bool]
        """
        return self._row_hidden
    
    @row_hidden.setter
    def row_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the rowHidden property value. Represents if all rows of the current range are hidden.
        Args:
            value: Value to set for the rowHidden property.
        """
        self._row_hidden = value
    
    @property
    def row_index(self,) -> Optional[int]:
        """
        Gets the rowIndex property value. Returns the row number of the first cell in the range. Zero-indexed. Read-only.
        Returns: Optional[int]
        """
        return self._row_index
    
    @row_index.setter
    def row_index(self,value: Optional[int] = None) -> None:
        """
        Sets the rowIndex property value. Returns the row number of the first cell in the range. Zero-indexed. Read-only.
        Args:
            value: Value to set for the rowIndex property.
        """
        self._row_index = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
        writer.write_object_value("values", self.values)
        writer.write_object_value("valueTypes", self.value_types)
        writer.write_object_value("worksheet", self.worksheet)
    
    @property
    def sort(self,) -> Optional[workbook_range_sort.WorkbookRangeSort]:
        """
        Gets the sort property value. The worksheet containing the current range. Read-only.
        Returns: Optional[workbook_range_sort.WorkbookRangeSort]
        """
        return self._sort
    
    @sort.setter
    def sort(self,value: Optional[workbook_range_sort.WorkbookRangeSort] = None) -> None:
        """
        Sets the sort property value. The worksheet containing the current range. Read-only.
        Args:
            value: Value to set for the sort property.
        """
        self._sort = value
    
    @property
    def text(self,) -> Optional[json.Json]:
        """
        Gets the text property value. Text values of the specified range. The Text value will not depend on the cell width. The # sign substitution that happens in Excel UI will not affect the text value returned by the API. Read-only.
        Returns: Optional[json.Json]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the text property value. Text values of the specified range. The Text value will not depend on the cell width. The # sign substitution that happens in Excel UI will not affect the text value returned by the API. Read-only.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    
    @property
    def values(self,) -> Optional[json.Json]:
        """
        Gets the values property value. Represents the raw values of the specified range. The data returned could be of type string, number, or a boolean. Cell that contain an error will return the error string.
        Returns: Optional[json.Json]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the values property value. Represents the raw values of the specified range. The data returned could be of type string, number, or a boolean. Cell that contain an error will return the error string.
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    
    @property
    def value_types(self,) -> Optional[json.Json]:
        """
        Gets the valueTypes property value. Represents the type of data of each cell. The possible values are: Unknown, Empty, String, Integer, Double, Boolean, Error. Read-only.
        Returns: Optional[json.Json]
        """
        return self._value_types
    
    @value_types.setter
    def value_types(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the valueTypes property value. Represents the type of data of each cell. The possible values are: Unknown, Empty, String, Integer, Double, Boolean, Error. Read-only.
        Args:
            value: Value to set for the valueTypes property.
        """
        self._value_types = value
    
    @property
    def worksheet(self,) -> Optional[workbook_worksheet.WorkbookWorksheet]:
        """
        Gets the worksheet property value. The worksheet containing the current range. Read-only.
        Returns: Optional[workbook_worksheet.WorkbookWorksheet]
        """
        return self._worksheet
    
    @worksheet.setter
    def worksheet(self,value: Optional[workbook_worksheet.WorkbookWorksheet] = None) -> None:
        """
        Sets the worksheet property value. The worksheet containing the current range. Read-only.
        Args:
            value: Value to set for the worksheet property.
        """
        self._worksheet = value
    

