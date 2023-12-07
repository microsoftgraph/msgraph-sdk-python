from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_compliance_policy_setting_state_summary import (
    DeviceCompliancePolicySettingStateSummary,
)


@dataclass
class DeviceCompliancePolicySettingStateSummaryCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceCompliancePolicySettingStateSummary]
):
    value: Optional[List[DeviceCompliancePolicySettingStateSummary]] = None

    def __init__(self):
        super().__init__(entity=DeviceCompliancePolicySettingStateSummary)
