from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ediscovery_review_set import EdiscoveryReviewSet


@dataclass
class EdiscoveryReviewSetCollectionResponse(
    BaseCollectionPaginationCountResponse[EdiscoveryReviewSet]
):
    value: Optional[List[EdiscoveryReviewSet]] = None

    def __init__(self):
        super().__init__(entity=EdiscoveryReviewSet)
