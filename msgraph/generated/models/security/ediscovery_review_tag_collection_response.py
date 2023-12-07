from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ediscovery_review_tag import EdiscoveryReviewTag


@dataclass
class EdiscoveryReviewTagCollectionResponse(
    BaseCollectionPaginationCountResponse[EdiscoveryReviewTag]
):
    value: Optional[List[EdiscoveryReviewTag]] = None

    def __init__(self):
        super().__init__(entity=EdiscoveryReviewTag)
