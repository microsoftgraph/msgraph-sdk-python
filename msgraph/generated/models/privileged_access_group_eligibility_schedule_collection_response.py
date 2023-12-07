from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule


@dataclass
class PrivilegedAccessGroupEligibilityScheduleCollectionResponse(
    BaseCollectionPaginationCountResponse[PrivilegedAccessGroupEligibilitySchedule]
):
    value: Optional[List[PrivilegedAccessGroupEligibilitySchedule]] = None

    def __init__(self):
        super().__init__(entity=PrivilegedAccessGroupEligibilitySchedule)
