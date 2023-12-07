from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .list_ import List_


@dataclass
class ListCollectionResponse(BaseCollectionPaginationCountResponse[List_]):
    value: Optional[List[List_]] = None

    def __init__(self):
        super().__init__(entity=List_)
