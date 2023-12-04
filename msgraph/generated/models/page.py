from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING, Dict, Callable, Any

from kiota_abstractions.serialization import ParseNode, SerializationWriter

if TYPE_CHECKING:
    from .base_item import BaseItem

from .base_item import BaseItem


@dataclass
class Page(BaseItem):
    id: Optional[str] = None
    title: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Page:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Page
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Page()

    def get_field_deserializers(self, ) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n: setattr(self, "id", n.get_str_value()),
            "title": lambda n: setattr(self, "title", n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    def serialize(self, writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("id", self.id)
        writer.write_str_value("title", self.title)
