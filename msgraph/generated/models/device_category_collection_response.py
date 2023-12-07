from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_category import DeviceCategory


@dataclass
class DeviceCategoryCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceCategory]
):
    value: Optional[List[DeviceCategory]] = None

    def __init__(self):
        super().__init__(entity=DeviceCategory)
