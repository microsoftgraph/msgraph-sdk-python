from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_e_book import ManagedEBook


@dataclass
class ManagedEBookCollectionResponse(
    BaseCollectionPaginationCountResponse[ManagedEBook]
):
    value: Optional[List[ManagedEBook]] = None

    def __init__(self):
        super().__init__(entity=ManagedEBook)
