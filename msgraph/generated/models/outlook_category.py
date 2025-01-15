from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .category_color import CategoryColor
    from .entity import Entity

from .entity import Entity

@dataclass
class OutlookCategory(Entity, Parsable):
    # A pre-set color constant that characterizes a category, and that is mapped to one of 25 predefined colors. For more details, see the following note.
    color: Optional[CategoryColor] = None
    # A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutlookCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutlookCategory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutlookCategory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .category_color import CategoryColor
        from .entity import Entity

        from .category_color import CategoryColor
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_enum_value(CategoryColor)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_enum_value("color", self.color)
        writer.write_str_value("displayName", self.display_name)
    

