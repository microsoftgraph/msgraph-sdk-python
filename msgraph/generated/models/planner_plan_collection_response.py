from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .planner_plan import PlannerPlan


@dataclass
class PlannerPlanCollectionResponse(BaseCollectionPaginationCountResponse[PlannerPlan]):
    value: Optional[List[PlannerPlan]] = None

    def __init__(self):
        super().__init__(entity=PlannerPlan)
