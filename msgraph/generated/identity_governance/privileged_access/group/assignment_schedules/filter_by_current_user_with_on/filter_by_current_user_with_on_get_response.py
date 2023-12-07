from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ......models.privileged_access_group_assignment_schedule import (
    PrivilegedAccessGroupAssignmentSchedule,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[PrivilegedAccessGroupAssignmentSchedule]
):
    value: Optional[List[PrivilegedAccessGroupAssignmentSchedule]] = None

    def __init__(self):
        super().__init__(entity=PrivilegedAccessGroupAssignmentSchedule)
