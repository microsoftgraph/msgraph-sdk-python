from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .privileged_access_group_eligibility_schedule_request import (
    PrivilegedAccessGroupEligibilityScheduleRequest,
)


@dataclass
class PrivilegedAccessGroupEligibilityScheduleRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[
        PrivilegedAccessGroupEligibilityScheduleRequest
    ]
):
    value: Optional[List[PrivilegedAccessGroupEligibilityScheduleRequest]] = None

    def __init__(self):
        super().__init__(entity=PrivilegedAccessGroupEligibilityScheduleRequest)
