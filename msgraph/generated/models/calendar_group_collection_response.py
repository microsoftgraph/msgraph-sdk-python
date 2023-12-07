from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .calendar_group import CalendarGroup


@dataclass
class CalendarGroupCollectionResponse(
    BaseCollectionPaginationCountResponse[CalendarGroup]
):
    value: Optional[List[CalendarGroup]] = None

    def __init__(self):
        super().__init__(entity=CalendarGroup)
