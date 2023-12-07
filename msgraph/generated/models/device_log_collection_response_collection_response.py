from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_log_collection_response import DeviceLogCollectionResponse


@dataclass
class DeviceLogCollectionResponseCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceLogCollectionResponse]
):
    value: Optional[List[DeviceLogCollectionResponse]] = None

    def __init__(self):
        super().__init__(entity=DeviceLogCollectionResponse)
