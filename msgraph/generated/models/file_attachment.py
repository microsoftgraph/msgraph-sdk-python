from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attachment = lazy_import('msgraph.generated.models.attachment')

class FileAttachment(attachment.Attachment):
    def __init__(self,) -> None:
        """
        Instantiates a new FileAttachment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.fileAttachment"
        # The base64-encoded contents of the file.
        self._content_bytes: Optional[bytes] = None
        # The ID of the attachment in the Exchange store.
        self._content_id: Optional[str] = None
        # Do not use this property as it is not supported.
        self._content_location: Optional[str] = None
    
    @property
    def content_bytes(self,) -> Optional[bytes]:
        """
        Gets the contentBytes property value. The base64-encoded contents of the file.
        Returns: Optional[bytes]
        """
        return self._content_bytes
    
    @content_bytes.setter
    def content_bytes(self,value: Optional[bytes] = None) -> None:
        """
        Sets the contentBytes property value. The base64-encoded contents of the file.
        Args:
            value: Value to set for the contentBytes property.
        """
        self._content_bytes = value
    
    @property
    def content_id(self,) -> Optional[str]:
        """
        Gets the contentId property value. The ID of the attachment in the Exchange store.
        Returns: Optional[str]
        """
        return self._content_id
    
    @content_id.setter
    def content_id(self,value: Optional[str] = None) -> None:
        """
        Sets the contentId property value. The ID of the attachment in the Exchange store.
        Args:
            value: Value to set for the contentId property.
        """
        self._content_id = value
    
    @property
    def content_location(self,) -> Optional[str]:
        """
        Gets the contentLocation property value. Do not use this property as it is not supported.
        Returns: Optional[str]
        """
        return self._content_location
    
    @content_location.setter
    def content_location(self,value: Optional[str] = None) -> None:
        """
        Sets the contentLocation property value. Do not use this property as it is not supported.
        Args:
            value: Value to set for the contentLocation property.
        """
        self._content_location = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileAttachment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FileAttachment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_bytes": lambda n : setattr(self, 'content_bytes', n.get_bytes_value()),
            "content_id": lambda n : setattr(self, 'content_id', n.get_str_value()),
            "content_location": lambda n : setattr(self, 'content_location', n.get_str_value()),
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
        writer.write_str_value("contentId", self.content_id)
        writer.write_str_value("contentLocation", self.content_location)
    

