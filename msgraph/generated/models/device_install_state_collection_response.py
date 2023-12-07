from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_install_state import DeviceInstallState


@dataclass
class DeviceInstallStateCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceInstallState]
):
    value: Optional[List[DeviceInstallState]] = None

    def __init__(self):
        super().__init__(entity=DeviceInstallState)
