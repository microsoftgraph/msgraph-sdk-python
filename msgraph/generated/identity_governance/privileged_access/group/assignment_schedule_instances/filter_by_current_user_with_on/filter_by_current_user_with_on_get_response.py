from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ......models.privileged_access_group_assignment_schedule_instance import (
    PrivilegedAccessGroupAssignmentScheduleInstance,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[
        PrivilegedAccessGroupAssignmentScheduleInstance
    ]
):
    value: Optional[List[PrivilegedAccessGroupAssignmentScheduleInstance]] = None

    def __init__(self):
        super().__init__(entity=PrivilegedAccessGroupAssignmentScheduleInstance)
