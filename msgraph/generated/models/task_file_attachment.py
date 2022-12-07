from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attachment_base = lazy_import('msgraph.generated.models.attachment_base')

class TaskFileAttachment(attachment_base.AttachmentBase):
    def __init__(self,) -> None:
        """
        Instantiates a new TaskFileAttachment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.taskFileAttachment"
        # The contentBytes property
        self._content_bytes: Optional[bytes] = None
    
    @property
    def content_bytes(self,) -> Optional[bytes]:
        """
        Gets the contentBytes property value. The contentBytes property
        Returns: Optional[bytes]
        """
        return self._content_bytes
    
    @content_bytes.setter
    def content_bytes(self,value: Optional[bytes] = None) -> None:
        """
        Sets the contentBytes property value. The contentBytes property
        Args:
            value: Value to set for the contentBytes property.
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
        fields = {
            "content_bytes": lambda n : setattr(self, 'content_bytes', n.get_bytes_value()),
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
    

