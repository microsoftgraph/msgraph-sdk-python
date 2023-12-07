from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ......models.privileged_access_group_assignment_schedule_request import (
    PrivilegedAccessGroupAssignmentScheduleRequest,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[
        PrivilegedAccessGroupAssignmentScheduleRequest
    ]
):
    value: Optional[List[PrivilegedAccessGroupAssignmentScheduleRequest]] = None

    def __init__(self):
        super().__init__(entity=PrivilegedAccessGroupAssignmentScheduleRequest)
