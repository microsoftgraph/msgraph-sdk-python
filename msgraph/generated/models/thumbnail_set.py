from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .thumbnail import Thumbnail

from .entity import Entity

@dataclass
class ThumbnailSet(Entity, Parsable):
    # A 1920x1920 scaled thumbnail.
    large: Optional[Thumbnail] = None
    # A 176x176 scaled thumbnail.
    medium: Optional[Thumbnail] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A 48x48 cropped thumbnail.
    small: Optional[Thumbnail] = None
    # A custom thumbnail image or the original image used to generate other thumbnails.
    source: Optional[Thumbnail] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThumbnailSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThumbnailSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ThumbnailSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .thumbnail import Thumbnail

        from .entity import Entity
        from .thumbnail import Thumbnail

        fields: dict[str, Callable[[Any], None]] = {
            "large": lambda n : setattr(self, 'large', n.get_object_value(Thumbnail)),
            "medium": lambda n : setattr(self, 'medium', n.get_object_value(Thumbnail)),
            "small": lambda n : setattr(self, 'small', n.get_object_value(Thumbnail)),
            "source": lambda n : setattr(self, 'source', n.get_object_value(Thumbnail)),
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
        writer.write_object_value("large", self.large)
        writer.write_object_value("medium", self.medium)
        writer.write_object_value("small", self.small)
        writer.write_object_value("source", self.source)
    

