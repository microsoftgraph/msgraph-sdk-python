from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_review_stage import AccessReviewStage
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessReviewStageCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessReviewStage]
):
    value: Optional[List[AccessReviewStage]] = None

    def __init__(self):
        super().__init__(entity=AccessReviewStage)
