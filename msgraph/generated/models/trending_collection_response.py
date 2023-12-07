from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .trending import Trending


@dataclass
class TrendingCollectionResponse(BaseCollectionPaginationCountResponse[Trending]):
    value: Optional[List[Trending]] = None

    def __init__(self):
        super().__init__(entity=Trending)
