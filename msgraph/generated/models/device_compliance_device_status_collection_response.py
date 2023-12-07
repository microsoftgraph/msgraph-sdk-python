from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_compliance_device_status import DeviceComplianceDeviceStatus


@dataclass
class DeviceComplianceDeviceStatusCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceComplianceDeviceStatus]
):
    value: Optional[List[DeviceComplianceDeviceStatus]] = None

    def __init__(self):
        super().__init__(entity=DeviceComplianceDeviceStatus)
