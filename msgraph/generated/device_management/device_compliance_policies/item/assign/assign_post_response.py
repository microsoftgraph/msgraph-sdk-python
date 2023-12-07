from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .....models.device_compliance_policy_assignment import DeviceCompliancePolicyAssignment


@dataclass
class AssignPostResponse(
    BaseCollectionPaginationCountResponse[DeviceCompliancePolicyAssignment]
):
    value: Optional[List[DeviceCompliancePolicyAssignment]] = None

    def __init__(self):
        super().__init__(entity=DeviceCompliancePolicyAssignment)
