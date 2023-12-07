from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment


@dataclass
class TargetedManagedAppPolicyAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[TargetedManagedAppPolicyAssignment]
):
    value: Optional[List[TargetedManagedAppPolicyAssignment]] = None

    def __init__(self):
        super().__init__(entity=TargetedManagedAppPolicyAssignment)
