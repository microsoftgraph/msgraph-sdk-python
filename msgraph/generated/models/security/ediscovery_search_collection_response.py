from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ediscovery_search import EdiscoverySearch


@dataclass
class EdiscoverySearchCollectionResponse(
    BaseCollectionPaginationCountResponse[EdiscoverySearch]
):
    value: Optional[List[EdiscoverySearch]] = None

    def __init__(self):
        super().__init__(entity=EdiscoverySearch)
