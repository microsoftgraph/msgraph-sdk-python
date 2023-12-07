from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .......models.security.ediscovery_review_tag import EdiscoveryReviewTag


@dataclass
class AsHierarchyGetResponse(
    BaseCollectionPaginationCountResponse[EdiscoveryReviewTag]
):
    value: Optional[List[EdiscoveryReviewTag]] = None

    def __init__(self):
        super().__init__(entity=EdiscoveryReviewTag)
