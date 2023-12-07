from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_configuration_state import DeviceConfigurationState


@dataclass
class DeviceConfigurationStateCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceConfigurationState]
):
    value: Optional[List[DeviceConfigurationState]] = None

    def __init__(self):
        super().__init__(entity=DeviceConfigurationState)
