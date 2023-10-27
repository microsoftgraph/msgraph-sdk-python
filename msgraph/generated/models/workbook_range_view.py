from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .json import Json

from .entity import Entity

@dataclass
class WorkbookRangeView(Entity):
    # Represents the cell addresses
    cell_addresses: Optional[Json] = None
    # Returns the number of visible columns. Read-only.
    column_count: Optional[int] = None
    # Represents the formula in A1-style notation.
    formulas: Optional[Json] = None
    # Represents the formula in A1-style notation, in the user's language and number-formatting locale. For example, the English '=SUM(A1, 1.5)' formula would become '=SUMME(A1; 1,5)' in German.
    formulas_local: Optional[Json] = None
    # Represents the formula in R1C1-style notation.
    formulas_r1_c1: Optional[Json] = None
    # Index of the range.
    index: Optional[int] = None
    # Represents Excel's number format code for the given cell. Read-only.
    number_format: Optional[Json] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Returns the number of visible rows. Read-only.
    row_count: Optional[int] = None
    # Represents a collection of range views associated with the range. Read-only. Read-only.
    rows: Optional[List[WorkbookRangeView]] = None
    # Text values of the specified range. The Text value won't depend on the cell width. The # sign substitution that happens in Excel UI won't affect the text value returned by the API. Read-only.
    text: Optional[Json] = None
    # Represents the type of data of each cell. Read-only. The possible values are: Unknown, Empty, String, Integer, Double, Boolean, Error.
    value_types: Optional[Json] = None
    # Represents the raw values of the specified range view. The data returned could be of type string, number, or a boolean. Cell that contains an error returns the error string.
    values: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookRangeView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookRangeView
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookRangeView()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .json import Json

        from .entity import Entity
        from .json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "cellAddresses": lambda n : setattr(self, 'cell_addresses', n.get_object_value(Json)),
            "columnCount": lambda n : setattr(self, 'column_count', n.get_int_value()),
            "formulas": lambda n : setattr(self, 'formulas', n.get_object_value(Json)),
            "formulasLocal": lambda n : setattr(self, 'formulas_local', n.get_object_value(Json)),
            "formulasR1C1": lambda n : setattr(self, 'formulas_r1_c1', n.get_object_value(Json)),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "numberFormat": lambda n : setattr(self, 'number_format', n.get_object_value(Json)),
            "rowCount": lambda n : setattr(self, 'row_count', n.get_int_value()),
            "rows": lambda n : setattr(self, 'rows', n.get_collection_of_object_values(WorkbookRangeView)),
            "text": lambda n : setattr(self, 'text', n.get_object_value(Json)),
            "valueTypes": lambda n : setattr(self, 'value_types', n.get_object_value(Json)),
            "values": lambda n : setattr(self, 'values', n.get_object_value(Json)),
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
        writer.write_object_value("valueTypes", self.value_types)
        writer.write_object_value("values", self.values)
    

