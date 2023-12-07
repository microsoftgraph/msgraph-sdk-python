from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .....models.unified_role_eligibility_schedule_request import (
    UnifiedRoleEligibilityScheduleRequest,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleEligibilityScheduleRequest]
):
    value: Optional[List[UnifiedRoleEligibilityScheduleRequest]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleEligibilityScheduleRequest)
