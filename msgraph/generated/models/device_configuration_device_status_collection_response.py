from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_configuration_device_status import DeviceConfigurationDeviceStatus


@dataclass
class DeviceConfigurationDeviceStatusCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceConfigurationDeviceStatus]
):
    value: Optional[List[DeviceConfigurationDeviceStatus]] = None

    def __init__(self):
        super().__init__(entity=DeviceConfigurationDeviceStatus)
