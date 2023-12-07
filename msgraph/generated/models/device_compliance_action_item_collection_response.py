from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_compliance_action_item import DeviceComplianceActionItem


@dataclass
class DeviceComplianceActionItemCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceComplianceActionItem]
):
    value: Optional[List[DeviceComplianceActionItem]] = None

    def __init__(self):
        super().__init__(entity=DeviceComplianceActionItem)
