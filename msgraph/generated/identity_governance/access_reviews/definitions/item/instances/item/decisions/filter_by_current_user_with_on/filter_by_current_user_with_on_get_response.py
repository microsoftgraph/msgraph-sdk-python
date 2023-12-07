from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .........models.access_review_instance_decision_item import AccessReviewInstanceDecisionItem
from .........models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[AccessReviewInstanceDecisionItem]
):
    value: Optional[List[AccessReviewInstanceDecisionItem]] = None

    def __init__(self):
        super().__init__(entity=AccessReviewInstanceDecisionItem)
