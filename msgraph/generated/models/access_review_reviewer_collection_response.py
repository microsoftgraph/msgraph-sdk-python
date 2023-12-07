from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_review_reviewer import AccessReviewReviewer
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessReviewReviewerCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessReviewReviewer]
):
    value: Optional[List[AccessReviewReviewer]] = None

    def __init__(self):
        super().__init__(entity=AccessReviewReviewer)
