from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .base_item import BaseItem


@dataclass
class BaseItemCollectionResponse(BaseCollectionPaginationCountResponse[BaseItem]):
    value: Optional[List[BaseItem]] = None

    def __init__(self):
        super().__init__(entity=BaseItem)
