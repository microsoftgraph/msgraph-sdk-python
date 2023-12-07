from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .scheduling_group import SchedulingGroup


@dataclass
class SchedulingGroupCollectionResponse(
    BaseCollectionPaginationCountResponse[SchedulingGroup]
):
    value: Optional[List[SchedulingGroup]] = None

    def __init__(self):
        super().__init__(entity=SchedulingGroup)
