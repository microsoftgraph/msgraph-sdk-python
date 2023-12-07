from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .print_service_endpoint import PrintServiceEndpoint


@dataclass
class PrintServiceEndpointCollectionResponse(
    BaseCollectionPaginationCountResponse[PrintServiceEndpoint]
):
    value: Optional[List[PrintServiceEndpoint]] = None

    def __init__(self):
        super().__init__(entity=PrintServiceEndpoint)
