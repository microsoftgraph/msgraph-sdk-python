from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .place import Place

from .place import Place

@dataclass
class Floor(Place, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.floor"
    # Specifies the sort order of the floor. For example, a floor might be named 'Lobby' with a sort order of 0 to show this floor first in ordered lists.
    sort_order: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Floor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Floor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Floor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .place import Place

        from .place import Place

        fields: dict[str, Callable[[Any], None]] = {
            "sortOrder": lambda n : setattr(self, 'sort_order', n.get_int_value()),
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
        writer.write_int_value("sortOrder", self.sort_order)
    

