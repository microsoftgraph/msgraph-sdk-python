from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .....models.unified_role_assignment_schedule_instance import (
    UnifiedRoleAssignmentScheduleInstance,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleAssignmentScheduleInstance]
):
    value: Optional[List[UnifiedRoleAssignmentScheduleInstance]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleAssignmentScheduleInstance)
