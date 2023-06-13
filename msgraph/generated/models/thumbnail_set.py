from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, thumbnail

from . import entity

@dataclass
class ThumbnailSet(entity.Entity):
    # A 1920x1920 scaled thumbnail.
    large: Optional[thumbnail.Thumbnail] = None
    # A 176x176 scaled thumbnail.
    medium: Optional[thumbnail.Thumbnail] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A 48x48 cropped thumbnail.
    small: Optional[thumbnail.Thumbnail] = None
    # A custom thumbnail image or the original image used to generate other thumbnails.
    source: Optional[thumbnail.Thumbnail] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThumbnailSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ThumbnailSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ThumbnailSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, thumbnail

        fields: Dict[str, Callable[[Any], None]] = {
            "large": lambda n : setattr(self, 'large', n.get_object_value(thumbnail.Thumbnail)),
            "medium": lambda n : setattr(self, 'medium', n.get_object_value(thumbnail.Thumbnail)),
            "small": lambda n : setattr(self, 'small', n.get_object_value(thumbnail.Thumbnail)),
            "source": lambda n : setattr(self, 'source', n.get_object_value(thumbnail.Thumbnail)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("large", self.large)
        writer.write_object_value("medium", self.medium)
        writer.write_object_value("small", self.small)
        writer.write_object_value("source", self.source)
    

