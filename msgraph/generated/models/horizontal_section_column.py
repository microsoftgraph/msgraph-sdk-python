from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .web_part import WebPart

from .entity import Entity

@dataclass
class HorizontalSectionColumn(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of WebParts in this column.
    webparts: Optional[list[WebPart]] = None
    # Width of the column. A horizontal section is divided into 12 grids. A column should have a value of 1-12 to represent its range spans. For example, there can be two columns both have a width of 6 in a section.
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HorizontalSectionColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HorizontalSectionColumn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HorizontalSectionColumn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .web_part import WebPart

        from .entity import Entity
        from .web_part import WebPart

        fields: dict[str, Callable[[Any], None]] = {
            "webparts": lambda n : setattr(self, 'webparts', n.get_collection_of_object_values(WebPart)),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
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
        writer.write_collection_of_object_values("webparts", self.webparts)
        writer.write_int_value("width", self.width)
    

