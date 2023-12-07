from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_review_schedule_definition import AccessReviewScheduleDefinition
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessReviewScheduleDefinitionCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessReviewScheduleDefinition]
):
    value: Optional[List[AccessReviewScheduleDefinition]] = None

    def __init__(self):
        super().__init__(entity=AccessReviewScheduleDefinition)
