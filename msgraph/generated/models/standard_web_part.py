from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .web_part import WebPart
    from .web_part_data import WebPartData

from .web_part import WebPart

@dataclass
class StandardWebPart(WebPart, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.standardWebPart"
    # The instance identifier of the container text webPart. It only works for inline standard webPart in rich text webParts.
    container_text_web_part_id: Optional[str] = None
    # Data of the webPart.
    data: Optional[WebPartData] = None
    # A Guid that indicates the webPart type.
    web_part_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StandardWebPart:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StandardWebPart
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StandardWebPart()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .web_part import WebPart
        from .web_part_data import WebPartData

        from .web_part import WebPart
        from .web_part_data import WebPartData

        fields: dict[str, Callable[[Any], None]] = {
            "containerTextWebPartId": lambda n : setattr(self, 'container_text_web_part_id', n.get_str_value()),
            "data": lambda n : setattr(self, 'data', n.get_object_value(WebPartData)),
            "webPartType": lambda n : setattr(self, 'web_part_type', n.get_str_value()),
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
        writer.write_str_value("containerTextWebPartId", self.container_text_web_part_id)
        writer.write_object_value("data", self.data)
        writer.write_str_value("webPartType", self.web_part_type)
    

