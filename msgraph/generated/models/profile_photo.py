from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ProfilePhoto(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new profilePhoto and sets the default values.
        """
        super().__init__()
        # The height of the photo. Read-only.
        self._height: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The width of the photo. Read-only.
        self._width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProfilePhoto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProfilePhoto
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProfilePhoto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def height(self,) -> Optional[int]:
        """
        Gets the height property value. The height of the photo. Read-only.
        Returns: Optional[int]
        """
        return self._height
    
    @height.setter
    def height(self,value: Optional[int] = None) -> None:
        """
        Sets the height property value. The height of the photo. Read-only.
        Args:
            value: Value to set for the height property.
        """
        self._height = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("height", self.height)
        writer.write_int_value("width", self.width)
    
    @property
    def width(self,) -> Optional[int]:
        """
        Gets the width property value. The width of the photo. Read-only.
        Returns: Optional[int]
        """
        return self._width
    
    @width.setter
    def width(self,value: Optional[int] = None) -> None:
        """
        Sets the width property value. The width of the photo. Read-only.
        Args:
            value: Value to set for the width property.
        """
        self._width = value
    

