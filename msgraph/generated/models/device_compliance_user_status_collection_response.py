from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_compliance_user_status import DeviceComplianceUserStatus


@dataclass
class DeviceComplianceUserStatusCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceComplianceUserStatus]
):
    value: Optional[List[DeviceComplianceUserStatus]] = None

    def __init__(self):
        super().__init__(entity=DeviceComplianceUserStatus)
