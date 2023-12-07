from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest


@dataclass
class UnifiedRoleAssignmentScheduleRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleAssignmentScheduleRequest]
):
    value: Optional[List[UnifiedRoleAssignmentScheduleRequest]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleAssignmentScheduleRequest)
