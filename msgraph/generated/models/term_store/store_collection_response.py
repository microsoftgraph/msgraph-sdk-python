from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .store import Store


@dataclass
class StoreCollectionResponse(BaseCollectionPaginationCountResponse[Store]):
    value: Optional[List[Store]] = None

    def __init__(self):
        super().__init__(entity=Store)
