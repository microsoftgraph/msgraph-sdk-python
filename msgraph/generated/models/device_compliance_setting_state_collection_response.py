from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_compliance_setting_state import DeviceComplianceSettingState


@dataclass
class DeviceComplianceSettingStateCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceComplianceSettingState]
):
    value: Optional[List[DeviceComplianceSettingState]] = None

    def __init__(self):
        super().__init__(entity=DeviceComplianceSettingState)
