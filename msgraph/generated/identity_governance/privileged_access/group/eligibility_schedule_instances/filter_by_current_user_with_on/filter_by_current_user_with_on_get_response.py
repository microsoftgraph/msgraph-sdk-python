from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ......models.privileged_access_group_eligibility_schedule_instance import (
    PrivilegedAccessGroupEligibilityScheduleInstance,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[
        PrivilegedAccessGroupEligibilityScheduleInstance
    ]
):
    value: Optional[List[PrivilegedAccessGroupEligibilityScheduleInstance]] = None

    def __init__(self):
        super().__init__(entity=PrivilegedAccessGroupEligibilityScheduleInstance)
