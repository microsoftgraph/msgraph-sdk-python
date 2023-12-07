from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TypeVar

from generated.models.base_collection_pagination_response import BaseCollectionPaginationResponse
from generated.models.entity import Entity
from kiota_abstractions.method import Method
from kiota_abstractions.request_information import RequestInformation

T = TypeVar("T", bound=Entity)


@dataclass
class BaseCollectionPaginationCountResponse(BaseCollectionPaginationResponse[T]):
    odata_count: Optional[int] = None

    def request_information(self, method: Method = Method.GET) -> RequestInformation:
        request_info = RequestInformation()
        request_info.url = self.odata_next_link
        request_info.http_method = method
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
