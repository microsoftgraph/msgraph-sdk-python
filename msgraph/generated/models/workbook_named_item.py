from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_worksheet import WorkbookWorksheet

from .entity import Entity

@dataclass
class WorkbookNamedItem(Entity, Parsable):
    # The comment associated with this name.
    comment: Optional[str] = None
    # The name of the object. Read-only.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the name is scoped to the workbook or to a specific worksheet. Read-only.
    scope: Optional[str] = None
    # The type of reference is associated with the name. The possible values are: String, Integer, Double, Boolean, Range. Read-only.
    type: Optional[str] = None
    # Indicates whether the object is visible.
    visible: Optional[bool] = None
    # Returns the worksheet to which the named item is scoped. Available only if the item is scoped to the worksheet. Read-only.
    worksheet: Optional[WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookNamedItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookNamedItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookNamedItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_worksheet import WorkbookWorksheet

        from .entity import Entity
        from .workbook_worksheet import WorkbookWorksheet

        fields: dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "visible": lambda n : setattr(self, 'visible', n.get_bool_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("name", self.name)
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("type", self.type)
        writer.write_bool_value("visible", self.visible)
        writer.write_object_value("worksheet", self.worksheet)
    

