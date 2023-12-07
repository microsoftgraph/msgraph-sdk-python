from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .domain import Domain


@dataclass
class DomainCollectionResponse(BaseCollectionPaginationCountResponse[Domain]):
    value: Optional[List[Domain]] = None

    def __init__(self):
        super().__init__(entity=Domain)
