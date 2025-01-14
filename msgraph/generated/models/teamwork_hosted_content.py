from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_message_hosted_content import ChatMessageHostedContent
    from .entity import Entity

from .entity import Entity

@dataclass
class TeamworkHostedContent(Entity, Parsable):
    # Write only. Bytes for the hosted content (such as images).
    content_bytes: Optional[bytes] = None
    # Write only. Content type. such as image/png, image/jpg.
    content_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkHostedContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkHostedContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessageHostedContent".casefold():
            from .chat_message_hosted_content import ChatMessageHostedContent

            return ChatMessageHostedContent()
        return TeamworkHostedContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chat_message_hosted_content import ChatMessageHostedContent
        from .entity import Entity

        from .chat_message_hosted_content import ChatMessageHostedContent
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "contentBytes": lambda n : setattr(self, 'content_bytes', n.get_bytes_value()),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
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
        writer.write_bytes_value("contentBytes", self.content_bytes)
        writer.write_str_value("contentType", self.content_type)
    

