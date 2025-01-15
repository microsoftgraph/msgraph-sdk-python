from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .onenote_entity_base_model import OnenoteEntityBaseModel

from .onenote_entity_base_model import OnenoteEntityBaseModel

@dataclass
class OnenoteResource(OnenoteEntityBaseModel, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onenoteResource"
    # The content stream
    content: Optional[bytes] = None
    # The URL for downloading the content
    content_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnenoteResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnenoteResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnenoteResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .onenote_entity_base_model import OnenoteEntityBaseModel

        from .onenote_entity_base_model import OnenoteEntityBaseModel

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "contentUrl": lambda n : setattr(self, 'content_url', n.get_str_value()),
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
        writer.write_bytes_value("content", self.content)
        writer.write_str_value("contentUrl", self.content_url)
    

