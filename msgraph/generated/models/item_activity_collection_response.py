from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .item_activity import ItemActivity


@dataclass
class ItemActivityCollectionResponse(
    BaseCollectionPaginationCountResponse[ItemActivity]
):
    value: Optional[List[ItemActivity]] = None

    def __init__(self):
        super().__init__(entity=ItemActivity)
