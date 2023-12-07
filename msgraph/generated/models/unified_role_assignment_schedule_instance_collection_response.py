from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance


@dataclass
class UnifiedRoleAssignmentScheduleInstanceCollectionResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleAssignmentScheduleInstance]
):
    value: Optional[List[UnifiedRoleAssignmentScheduleInstance]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleAssignmentScheduleInstance)
