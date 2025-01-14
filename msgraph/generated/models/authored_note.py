from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity import Identity
    from .item_body import ItemBody

from .entity import Entity

@dataclass
class AuthoredNote(Entity, Parsable):
    # Identity information about the note's author.
    author: Optional[Identity] = None
    # The content of the note.
    content: Optional[ItemBody] = None
    # The date and time when the entity was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthoredNote:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthoredNote
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthoredNote()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity import Identity
        from .item_body import ItemBody

        from .entity import Entity
        from .identity import Identity
        from .item_body import ItemBody

        fields: dict[str, Callable[[Any], None]] = {
            "author": lambda n : setattr(self, 'author', n.get_object_value(Identity)),
            "content": lambda n : setattr(self, 'content', n.get_object_value(ItemBody)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
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
        writer.write_object_value("author", self.author)
        writer.write_object_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
    

