from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class AiInteractionAttachment(Entity, Parsable):
    # The identifier for the attachment. This identifier is only unique within the message scope.
    attachment_id: Optional[str] = None
    # The content of the attachment.
    content: Optional[str] = None
    # The type of the content. For example, reference, file, and image/imageType.
    content_type: Optional[str] = None
    # The URL of the content.
    content_url: Optional[str] = None
    # The name of the attachment.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AiInteractionAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AiInteractionAttachment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AiInteractionAttachment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "attachmentId": lambda n : setattr(self, 'attachment_id', n.get_str_value()),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "contentUrl": lambda n : setattr(self, 'content_url', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("attachmentId", self.attachment_id)
        writer.write_str_value("content", self.content)
        writer.write_str_value("contentType", self.content_type)
        writer.write_str_value("contentUrl", self.content_url)
        writer.write_str_value("name", self.name)
    

