from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .set import Set


@dataclass
class SetCollectionResponse(BaseCollectionPaginationCountResponse[Set]):
    value: Optional[List[Set]] = None

    def __init__(self):
        super().__init__(entity=Set)
