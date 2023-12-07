from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .target_device_group import TargetDeviceGroup


@dataclass
class TargetDeviceGroupCollectionResponse(
    BaseCollectionPaginationCountResponse[TargetDeviceGroup]
):
    value: Optional[List[TargetDeviceGroup]] = None

    def __init__(self):
        super().__init__(entity=TargetDeviceGroup)
