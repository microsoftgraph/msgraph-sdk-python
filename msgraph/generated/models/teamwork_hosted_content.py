from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class TeamworkHostedContent(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkHostedContent and sets the default values.
        """
        super().__init__()
        # Write only. Bytes for the hosted content (such as images).
        self._content_bytes: Optional[bytes] = None
        # Write only. Content type. sicj as image/png, image/jpg.
        self._content_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def content_bytes(self,) -> Optional[bytes]:
        """
        Gets the contentBytes property value. Write only. Bytes for the hosted content (such as images).
        Returns: Optional[bytes]
        """
        return self._content_bytes
    
    @content_bytes.setter
    def content_bytes(self,value: Optional[bytes] = None) -> None:
        """
        Sets the contentBytes property value. Write only. Bytes for the hosted content (such as images).
        Args:
            value: Value to set for the contentBytes property.
        """
        self._content_bytes = value
    
    @property
    def content_type(self,) -> Optional[str]:
        """
        Gets the contentType property value. Write only. Content type. sicj as image/png, image/jpg.
        Returns: Optional[str]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[str] = None) -> None:
        """
        Sets the contentType property value. Write only. Content type. sicj as image/png, image/jpg.
        Args:
            value: Value to set for the contentType property.
        """
        self._content_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkHostedContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkHostedContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkHostedContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_bytes": lambda n : setattr(self, 'content_bytes', n.get_bytes_value()),
            "content_type": lambda n : setattr(self, 'content_type', n.get_str_value()),
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
        writer.write_object_value("contentBytes", self.content_bytes)
        writer.write_str_value("contentType", self.content_type)
    

