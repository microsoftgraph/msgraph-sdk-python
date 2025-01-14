from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class WorkbookRangeView(Entity, Parsable):
    # The number of visible columns. Read-only.
    column_count: Optional[int] = None
    # The index of the range.
    index: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of visible rows. Read-only.
    row_count: Optional[int] = None
    # The collection of range views associated with the range. Read-only. Read-only.
    rows: Optional[list[WorkbookRangeView]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookRangeView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookRangeView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookRangeView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "columnCount": lambda n : setattr(self, 'column_count', n.get_int_value()),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "rowCount": lambda n : setattr(self, 'row_count', n.get_int_value()),
            "rows": lambda n : setattr(self, 'rows', n.get_collection_of_object_values(WorkbookRangeView)),
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
        writer.write_int_value("columnCount", self.column_count)
        writer.write_int_value("index", self.index)
        writer.write_int_value("rowCount", self.row_count)
        writer.write_collection_of_object_values("rows", self.rows)
    

