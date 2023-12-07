from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest


@dataclass
class UnifiedRoleEligibilityScheduleRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleEligibilityScheduleRequest]
):
    value: Optional[List[UnifiedRoleEligibilityScheduleRequest]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleEligibilityScheduleRequest)
