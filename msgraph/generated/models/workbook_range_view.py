from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
json = lazy_import('msgraph.generated.models.json')

class WorkbookRangeView(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def cell_addresses(self,) -> Optional[json.Json]:
        """
        Gets the cellAddresses property value. Represents the cell addresses
        Returns: Optional[json.Json]
        """
        return self._cell_addresses
    
    @cell_addresses.setter
    def cell_addresses(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the cellAddresses property value. Represents the cell addresses
        Args:
            value: Value to set for the cellAddresses property.
        """
        self._cell_addresses = value
    
    @property
    def column_count(self,) -> Optional[int]:
        """
        Gets the columnCount property value. Returns the number of visible columns. Read-only.
        Returns: Optional[int]
        """
        return self._column_count
    
    @column_count.setter
    def column_count(self,value: Optional[int] = None) -> None:
        """
        Sets the columnCount property value. Returns the number of visible columns. Read-only.
        Args:
            value: Value to set for the columnCount property.
        """
        self._column_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookRangeView and sets the default values.
        """
        super().__init__()
        # Represents the cell addresses
        self._cell_addresses: Optional[json.Json] = None
        # Returns the number of visible columns. Read-only.
        self._column_count: Optional[int] = None
        # Represents the formula in A1-style notation.
        self._formulas: Optional[json.Json] = None
        # Represents the formula in A1-style notation, in the user's language and number-formatting locale. For example, the English '=SUM(A1, 1.5)' formula would become '=SUMME(A1; 1,5)' in German.
        self._formulas_local: Optional[json.Json] = None
        # Represents the formula in R1C1-style notation.
        self._formulas_r1_c1: Optional[json.Json] = None
        # Index of the range.
        self._index: Optional[int] = None
        # Represents Excel's number format code for the given cell. Read-only.
        self._number_format: Optional[json.Json] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Returns the number of visible rows. Read-only.
        self._row_count: Optional[int] = None
        # Represents a collection of range views associated with the range. Read-only. Read-only.
        self._rows: Optional[List[WorkbookRangeView]] = None
        # Text values of the specified range. The Text value will not depend on the cell width. The # sign substitution that happens in Excel UI will not affect the text value returned by the API. Read-only.
        self._text: Optional[json.Json] = None
        # Represents the raw values of the specified range view. The data returned could be of type string, number, or a boolean. Cell that contain an error will return the error string.
        self._values: Optional[json.Json] = None
        # Represents the type of data of each cell. Read-only. The possible values are: Unknown, Empty, String, Integer, Double, Boolean, Error.
        self._value_types: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookRangeView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookRangeView
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookRangeView()
    
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
        Gets the formulasLocal property value. Represents the formula in A1-style notation, in the user's language and number-formatting locale. For example, the English '=SUM(A1, 1.5)' formula would become '=SUMME(A1; 1,5)' in German.
        Returns: Optional[json.Json]
        """
        return self._formulas_local
    
    @formulas_local.setter
    def formulas_local(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the formulasLocal property value. Represents the formula in A1-style notation, in the user's language and number-formatting locale. For example, the English '=SUM(A1, 1.5)' formula would become '=SUMME(A1; 1,5)' in German.
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
            "cell_addresses": lambda n : setattr(self, 'cell_addresses', n.get_object_value(json.Json)),
            "column_count": lambda n : setattr(self, 'column_count', n.get_int_value()),
            "formulas": lambda n : setattr(self, 'formulas', n.get_object_value(json.Json)),
            "formulas_local": lambda n : setattr(self, 'formulas_local', n.get_object_value(json.Json)),
            "formulas_r1_c1": lambda n : setattr(self, 'formulas_r1_c1', n.get_object_value(json.Json)),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "number_format": lambda n : setattr(self, 'number_format', n.get_object_value(json.Json)),
            "row_count": lambda n : setattr(self, 'row_count', n.get_int_value()),
            "rows": lambda n : setattr(self, 'rows', n.get_collection_of_object_values(WorkbookRangeView)),
            "text": lambda n : setattr(self, 'text', n.get_object_value(json.Json)),
            "values": lambda n : setattr(self, 'values', n.get_object_value(json.Json)),
            "value_types": lambda n : setattr(self, 'value_types', n.get_object_value(json.Json)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def index(self,) -> Optional[int]:
        """
        Gets the index property value. Index of the range.
        Returns: Optional[int]
        """
        return self._index
    
    @index.setter
    def index(self,value: Optional[int] = None) -> None:
        """
        Sets the index property value. Index of the range.
        Args:
            value: Value to set for the index property.
        """
        self._index = value
    
    @property
    def number_format(self,) -> Optional[json.Json]:
        """
        Gets the numberFormat property value. Represents Excel's number format code for the given cell. Read-only.
        Returns: Optional[json.Json]
        """
        return self._number_format
    
    @number_format.setter
    def number_format(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the numberFormat property value. Represents Excel's number format code for the given cell. Read-only.
        Args:
            value: Value to set for the numberFormat property.
        """
        self._number_format = value
    
    @property
    def row_count(self,) -> Optional[int]:
        """
        Gets the rowCount property value. Returns the number of visible rows. Read-only.
        Returns: Optional[int]
        """
        return self._row_count
    
    @row_count.setter
    def row_count(self,value: Optional[int] = None) -> None:
        """
        Sets the rowCount property value. Returns the number of visible rows. Read-only.
        Args:
            value: Value to set for the rowCount property.
        """
        self._row_count = value
    
    @property
    def rows(self,) -> Optional[List[WorkbookRangeView]]:
        """
        Gets the rows property value. Represents a collection of range views associated with the range. Read-only. Read-only.
        Returns: Optional[List[WorkbookRangeView]]
        """
        return self._rows
    
    @rows.setter
    def rows(self,value: Optional[List[WorkbookRangeView]] = None) -> None:
        """
        Sets the rows property value. Represents a collection of range views associated with the range. Read-only. Read-only.
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
        writer.write_object_value("cellAddresses", self.cell_addresses)
        writer.write_int_value("columnCount", self.column_count)
        writer.write_object_value("formulas", self.formulas)
        writer.write_object_value("formulasLocal", self.formulas_local)
        writer.write_object_value("formulasR1C1", self.formulas_r1_c1)
        writer.write_int_value("index", self.index)
        writer.write_object_value("numberFormat", self.number_format)
        writer.write_int_value("rowCount", self.row_count)
        writer.write_collection_of_object_values("rows", self.rows)
        writer.write_object_value("text", self.text)
        writer.write_object_value("values", self.values)
        writer.write_object_value("valueTypes", self.value_types)
    
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
        Gets the values property value. Represents the raw values of the specified range view. The data returned could be of type string, number, or a boolean. Cell that contain an error will return the error string.
        Returns: Optional[json.Json]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the values property value. Represents the raw values of the specified range view. The data returned could be of type string, number, or a boolean. Cell that contain an error will return the error string.
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    
    @property
    def value_types(self,) -> Optional[json.Json]:
        """
        Gets the valueTypes property value. Represents the type of data of each cell. Read-only. The possible values are: Unknown, Empty, String, Integer, Double, Boolean, Error.
        Returns: Optional[json.Json]
        """
        return self._value_types
    
    @value_types.setter
    def value_types(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the valueTypes property value. Represents the type of data of each cell. Read-only. The possible values are: Unknown, Empty, String, Integer, Double, Boolean, Error.
        Args:
            value: Value to set for the valueTypes property.
        """
        self._value_types = value
    

