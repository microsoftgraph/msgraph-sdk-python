from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ......models.privileged_access_group_eligibility_schedule_request import (
    PrivilegedAccessGroupEligibilityScheduleRequest,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[
        PrivilegedAccessGroupEligibilityScheduleRequest
    ]
):
    value: Optional[List[PrivilegedAccessGroupEligibilityScheduleRequest]] = None

    def __init__(self):
        super().__init__(entity=PrivilegedAccessGroupEligibilityScheduleRequest)
