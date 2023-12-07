from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_review_history_instance import AccessReviewHistoryInstance
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessReviewHistoryInstanceCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessReviewHistoryInstance]
):
    value: Optional[List[AccessReviewHistoryInstance]] = None

    def __init__(self):
        super().__init__(entity=AccessReviewHistoryInstance)
