from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional, TypeVar

from kiota_abstractions.method import Method
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.serialization import ParseNode, SerializationWriter

from generated.models.base_collection_pagination_response import BaseCollectionPaginationResponse
from generated.models.entity import Entity

T = TypeVar('T', bound=Entity)


@dataclass
class BaseCollectionPaginationCountResponse(BaseCollectionPaginationResponse[T]):
    # The OdataCount property
    odata_count: Optional[int] = None
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.count": lambda n : setattr(self, 'odata_count', n.get_int_value()),
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
        writer.write_int_value("@odata.count", self.odata_count)

    def request_information(self, method: Method = Method.GET) -> RequestInformation:
        request_info = RequestInformation()
        request_info.url = self.odata_next_link
        request_info.http_method = method
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
