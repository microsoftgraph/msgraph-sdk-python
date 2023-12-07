from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .planner_bucket import PlannerBucket


@dataclass
class PlannerBucketCollectionResponse(
    BaseCollectionPaginationCountResponse[PlannerBucket]
):
    value: Optional[List[PlannerBucket]] = None

    def __init__(self):
        super().__init__(entity=PlannerBucket)
