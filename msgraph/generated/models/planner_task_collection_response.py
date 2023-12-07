from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .planner_task import PlannerTask


@dataclass
class PlannerTaskCollectionResponse(BaseCollectionPaginationCountResponse[PlannerTask]):
    value: Optional[List[PlannerTask]] = None

    def __init__(self):
        super().__init__(entity=PlannerTask)
