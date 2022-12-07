from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

base_item_version = lazy_import('msgraph.generated.models.base_item_version')

class DriveItemVersion(base_item_version.BaseItemVersion):
    def __init__(self,) -> None:
        """
        Instantiates a new DriveItemVersion and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.driveItemVersion"
        # The content stream for this version of the item.
        self._content: Optional[bytes] = None
        # Indicates the size of the content stream for this version of the item.
        self._size: Optional[int] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The content stream for this version of the item.
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The content stream for this version of the item.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DriveItemVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DriveItemVersion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DriveItemVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_object_value("content", self.content)
        writer.write_int_value("size", self.size)
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. Indicates the size of the content stream for this version of the item.
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. Indicates the size of the content stream for this version of the item.
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    

