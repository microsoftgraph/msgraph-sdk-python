from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .....models.unified_role_assignment_schedule_request import (
    UnifiedRoleAssignmentScheduleRequest,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleAssignmentScheduleRequest]
):
    value: Optional[List[UnifiedRoleAssignmentScheduleRequest]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleAssignmentScheduleRequest)
