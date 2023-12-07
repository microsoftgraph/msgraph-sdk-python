from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .privileged_access_group_assignment_schedule_instance import (
    PrivilegedAccessGroupAssignmentScheduleInstance,
)


@dataclass
class PrivilegedAccessGroupAssignmentScheduleInstanceCollectionResponse(
    BaseCollectionPaginationCountResponse[
        PrivilegedAccessGroupAssignmentScheduleInstance
    ]
):
    value: Optional[List[PrivilegedAccessGroupAssignmentScheduleInstance]] = None

    def __init__(self):
        super().__init__(entity=PrivilegedAccessGroupAssignmentScheduleInstance)
