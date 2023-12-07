from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .unified_role_management_policy import UnifiedRoleManagementPolicy


@dataclass
class UnifiedRoleManagementPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleManagementPolicy]
):
    value: Optional[List[UnifiedRoleManagementPolicy]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleManagementPolicy)
