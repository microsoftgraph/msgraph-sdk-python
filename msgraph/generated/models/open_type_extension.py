from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .extension import Extension

from .extension import Extension

@dataclass
class OpenTypeExtension(Extension, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.openTypeExtension"
    # A unique text identifier for an open type data extension. Optional.
    extension_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OpenTypeExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OpenTypeExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OpenTypeExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .extension import Extension

        from .extension import Extension

        fields: dict[str, Callable[[Any], None]] = {
            "extensionName": lambda n : setattr(self, 'extension_name', n.get_str_value()),
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
        writer.write_str_value("extensionName", self.extension_name)
    

