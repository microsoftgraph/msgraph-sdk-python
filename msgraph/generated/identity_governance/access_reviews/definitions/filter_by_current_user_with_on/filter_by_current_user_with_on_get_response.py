from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.access_review_schedule_definition import AccessReviewScheduleDefinition
from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[AccessReviewScheduleDefinition]
):
    value: Optional[List[AccessReviewScheduleDefinition]] = None

    def __init__(self):
        super().__init__(entity=AccessReviewScheduleDefinition)
