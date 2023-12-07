from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule


@dataclass
class UnifiedRoleEligibilityScheduleCollectionResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleEligibilitySchedule]
):
    value: Optional[List[UnifiedRoleEligibilitySchedule]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleEligibilitySchedule)
