from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_item_version import BaseItemVersion

from .base_item_version import BaseItemVersion

@dataclass
class DriveItemVersion(BaseItemVersion, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.driveItemVersion"
    # The content stream for this version of the item.
    content: Optional[bytes] = None
    # Indicates the size of the content stream for this version of the item.
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriveItemVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriveItemVersion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DriveItemVersion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_item_version import BaseItemVersion

        from .base_item_version import BaseItemVersion

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_int_value("size", self.size)
    

