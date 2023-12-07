from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .calendar_permission import CalendarPermission


@dataclass
class CalendarPermissionCollectionResponse(
    BaseCollectionPaginationCountResponse[CalendarPermission]
):
    value: Optional[List[CalendarPermission]] = None

    def __init__(self):
        super().__init__(entity=CalendarPermission)
