from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .endpoint import Endpoint


@dataclass
class EndpointCollectionResponse(BaseCollectionPaginationCountResponse[Endpoint]):
    value: Optional[List[Endpoint]] = None

    def __init__(self):
        super().__init__(entity=Endpoint)
