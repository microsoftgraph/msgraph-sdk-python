from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING

from kiota_abstractions.serialization import ParseNode, SerializationWriter

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse

if TYPE_CHECKING:
    from .page import Page


@dataclass
class SitePagesCollectionResponse(BaseCollectionPaginationCountResponse):
    # The value property
    value: Optional[List[Page]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SitePagesCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SitePagesCollectionResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SitePagesCollectionResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """

        from .page import Page

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(Page)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("value", self.value)
