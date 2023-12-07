from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_device_mobile_app_configuration_device_status import (
    ManagedDeviceMobileAppConfigurationDeviceStatus,
)


@dataclass
class ManagedDeviceMobileAppConfigurationDeviceStatusCollectionResponse(
    BaseCollectionPaginationCountResponse[
        ManagedDeviceMobileAppConfigurationDeviceStatus
    ]
):
    value: Optional[List[ManagedDeviceMobileAppConfigurationDeviceStatus]] = None

    def __init__(self):
        super().__init__(entity=ManagedDeviceMobileAppConfigurationDeviceStatus)
