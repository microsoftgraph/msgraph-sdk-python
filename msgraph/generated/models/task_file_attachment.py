from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attachment_base

from . import attachment_base

class TaskFileAttachment(attachment_base.AttachmentBase):
    def __init__(self,) -> None:
        """
        Instantiates a new TaskFileAttachment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.taskFileAttachment"
        # The base64-encoded contents of the file.
        self._content_bytes: Optional[bytes] = None
    
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
            value: Value to set for the content_bytes property.
        """
        self._content_bytes = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TaskFileAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TaskFileAttachment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TaskFileAttachment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attachment_base

        fields: Dict[str, Callable[[Any], None]] = {
            "contentBytes": lambda n : setattr(self, 'content_bytes', n.get_bytes_value()),
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
    

