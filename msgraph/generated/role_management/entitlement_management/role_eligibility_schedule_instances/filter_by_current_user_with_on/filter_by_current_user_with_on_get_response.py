from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .....models.unified_role_eligibility_schedule_instance import (
    UnifiedRoleEligibilityScheduleInstance,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleEligibilityScheduleInstance]
):
    value: Optional[List[UnifiedRoleEligibilityScheduleInstance]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleEligibilityScheduleInstance)
