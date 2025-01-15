from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .channel import Channel
    from .entity import Entity

from .entity import Entity

@dataclass
class DeletedTeam(Entity, Parsable):
    # The channels that are either shared with this deleted team or created in this deleted team.
    channels: Optional[list[Channel]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeletedTeam:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeletedTeam
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeletedTeam()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .channel import Channel
        from .entity import Entity

        from .channel import Channel
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "channels": lambda n : setattr(self, 'channels', n.get_collection_of_object_values(Channel)),
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
        writer.write_collection_of_object_values("channels", self.channels)
    

