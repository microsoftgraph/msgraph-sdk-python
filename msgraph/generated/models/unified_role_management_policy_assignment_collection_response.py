from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment


@dataclass
class UnifiedRoleManagementPolicyAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleManagementPolicyAssignment]
):
    value: Optional[List[UnifiedRoleManagementPolicyAssignment]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleManagementPolicyAssignment)
