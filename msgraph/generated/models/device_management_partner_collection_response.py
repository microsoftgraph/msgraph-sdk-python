from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_management_partner import DeviceManagementPartner


@dataclass
class DeviceManagementPartnerCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceManagementPartner]
):
    value: Optional[List[DeviceManagementPartner]] = None

    def __init__(self):
        super().__init__(entity=DeviceManagementPartner)
