from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ...models.search_response import SearchResponse


@dataclass
class QueryPostResponse(BaseCollectionPaginationCountResponse[SearchResponse]):
    value: Optional[List[SearchResponse]] = None

    def __init__(self):
        super().__init__(entity=SearchResponse)
