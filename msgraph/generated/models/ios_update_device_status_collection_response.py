from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ios_update_device_status import IosUpdateDeviceStatus


@dataclass
class IosUpdateDeviceStatusCollectionResponse(
    BaseCollectionPaginationCountResponse[IosUpdateDeviceStatus]
):
    value: Optional[List[IosUpdateDeviceStatus]] = None

    def __init__(self):
        super().__init__(entity=IosUpdateDeviceStatus)
