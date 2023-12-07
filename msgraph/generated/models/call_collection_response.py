from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .call import Call


@dataclass
class CallCollectionResponse(BaseCollectionPaginationCountResponse[Call]):
    value: Optional[List[Call]] = None

    def __init__(self):
        super().__init__(entity=Call)
