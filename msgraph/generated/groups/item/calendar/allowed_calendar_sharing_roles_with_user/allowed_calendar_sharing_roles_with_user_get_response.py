from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .....models.calendar_role_type import CalendarRoleType


@dataclass
class AllowedCalendarSharingRolesWithUserGetResponse(
    BaseCollectionPaginationCountResponse[CalendarRoleType]
):
    value: Optional[List[CalendarRoleType]] = None

    def __init__(self):
        super().__init__(entity=CalendarRoleType)
