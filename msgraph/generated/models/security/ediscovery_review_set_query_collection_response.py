from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ediscovery_review_set_query import EdiscoveryReviewSetQuery


@dataclass
class EdiscoveryReviewSetQueryCollectionResponse(
    BaseCollectionPaginationCountResponse[EdiscoveryReviewSetQuery]
):
    value: Optional[List[EdiscoveryReviewSetQuery]] = None

    def __init__(self):
        super().__init__(entity=EdiscoveryReviewSetQuery)
