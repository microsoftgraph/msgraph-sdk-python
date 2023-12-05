from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional, TypeVar

from kiota_abstractions.serialization import ParseNode, SerializationWriter

from generated.models.base_collection_pagination_response import BaseCollectionPaginationResponse
from generated.models.entity import Entity

T = TypeVar('T', bound=Entity)


@dataclass
class BaseDeltaFunctionResponse(BaseCollectionPaginationResponse[T]):
    # The OdataDeltaLink property
    odata_delta_link: Optional[str] = None
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.deltaLink": lambda n : setattr(self, 'odata_delta_link', n.get_str_value()),
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
        writer.write_str_value("@odata.deltaLink", self.odata_delta_link)
