from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_compliance_policy_state import DeviceCompliancePolicyState


@dataclass
class DeviceCompliancePolicyStateCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceCompliancePolicyState]
):
    value: Optional[List[DeviceCompliancePolicyState]] = None

    def __init__(self):
        super().__init__(entity=DeviceCompliancePolicyState)
