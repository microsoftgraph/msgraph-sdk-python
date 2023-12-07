from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule


@dataclass
class DeviceComplianceScheduledActionForRuleCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceComplianceScheduledActionForRule]
):
    value: Optional[List[DeviceComplianceScheduledActionForRule]] = None

    def __init__(self):
        super().__init__(entity=DeviceComplianceScheduledActionForRule)
