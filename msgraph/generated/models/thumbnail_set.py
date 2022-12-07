from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
thumbnail = lazy_import('msgraph.generated.models.thumbnail')

class ThumbnailSet(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new thumbnailSet and sets the default values.
        """
        super().__init__()
        # A 1920x1920 scaled thumbnail.
        self._large: Optional[thumbnail.Thumbnail] = None
        # A 176x176 scaled thumbnail.
        self._medium: Optional[thumbnail.Thumbnail] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A 48x48 cropped thumbnail.
        self._small: Optional[thumbnail.Thumbnail] = None
        # A custom thumbnail image or the original image used to generate other thumbnails.
        self._source: Optional[thumbnail.Thumbnail] = None
    
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
        fields = {
            "large": lambda n : setattr(self, 'large', n.get_object_value(thumbnail.Thumbnail)),
            "medium": lambda n : setattr(self, 'medium', n.get_object_value(thumbnail.Thumbnail)),
            "small": lambda n : setattr(self, 'small', n.get_object_value(thumbnail.Thumbnail)),
            "source": lambda n : setattr(self, 'source', n.get_object_value(thumbnail.Thumbnail)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def large(self,) -> Optional[thumbnail.Thumbnail]:
        """
        Gets the large property value. A 1920x1920 scaled thumbnail.
        Returns: Optional[thumbnail.Thumbnail]
        """
        return self._large
    
    @large.setter
    def large(self,value: Optional[thumbnail.Thumbnail] = None) -> None:
        """
        Sets the large property value. A 1920x1920 scaled thumbnail.
        Args:
            value: Value to set for the large property.
        """
        self._large = value
    
    @property
    def medium(self,) -> Optional[thumbnail.Thumbnail]:
        """
        Gets the medium property value. A 176x176 scaled thumbnail.
        Returns: Optional[thumbnail.Thumbnail]
        """
        return self._medium
    
    @medium.setter
    def medium(self,value: Optional[thumbnail.Thumbnail] = None) -> None:
        """
        Sets the medium property value. A 176x176 scaled thumbnail.
        Args:
            value: Value to set for the medium property.
        """
        self._medium = value
    
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
    
    @property
    def small(self,) -> Optional[thumbnail.Thumbnail]:
        """
        Gets the small property value. A 48x48 cropped thumbnail.
        Returns: Optional[thumbnail.Thumbnail]
        """
        return self._small
    
    @small.setter
    def small(self,value: Optional[thumbnail.Thumbnail] = None) -> None:
        """
        Sets the small property value. A 48x48 cropped thumbnail.
        Args:
            value: Value to set for the small property.
        """
        self._small = value
    
    @property
    def source(self,) -> Optional[thumbnail.Thumbnail]:
        """
        Gets the source property value. A custom thumbnail image or the original image used to generate other thumbnails.
        Returns: Optional[thumbnail.Thumbnail]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[thumbnail.Thumbnail] = None) -> None:
        """
        Sets the source property value. A custom thumbnail image or the original image used to generate other thumbnails.
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    

