from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule


@dataclass
class UnifiedRoleAssignmentScheduleCollectionResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleAssignmentSchedule]
):
    value: Optional[List[UnifiedRoleAssignmentSchedule]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleAssignmentSchedule)
