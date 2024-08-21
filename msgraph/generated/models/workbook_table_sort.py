from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_sort_field import WorkbookSortField

from .entity import Entity

@dataclass
class WorkbookTableSort(Entity):
    # The list of the current conditions last used to sort the table. Read-only.
    fields: Optional[List[WorkbookSortField]] = None
    # Indicates whether the casing impacted the last sort of the table. Read-only.
    match_case: Optional[bool] = None
    # The Chinese character ordering method last used to sort the table. The possible values are: PinYin, StrokeCount. Read-only.
    method: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookTableSort:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookTableSort
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookTableSort()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_sort_field import WorkbookSortField

        from .entity import Entity
        from .workbook_sort_field import WorkbookSortField

        fields: Dict[str, Callable[[Any], None]] = {
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_object_values(WorkbookSortField)),
            "matchCase": lambda n : setattr(self, 'match_case', n.get_bool_value()),
            "method": lambda n : setattr(self, 'method', n.get_str_value()),
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
        writer.write_collection_of_object_values("fields", self.fields)
        writer.write_bool_value("matchCase", self.match_case)
        writer.write_str_value("method", self.method)
    

