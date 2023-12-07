from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_compliance_policy import DeviceCompliancePolicy


@dataclass
class DeviceCompliancePolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceCompliancePolicy]
):
    value: Optional[List[DeviceCompliancePolicy]] = None

    def __init__(self):
        super().__init__(entity=DeviceCompliancePolicy)
