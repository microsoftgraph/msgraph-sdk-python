from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance


@dataclass
class UnifiedRoleEligibilityScheduleInstanceCollectionResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleEligibilityScheduleInstance]
):
    value: Optional[List[UnifiedRoleEligibilityScheduleInstance]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleEligibilityScheduleInstance)
