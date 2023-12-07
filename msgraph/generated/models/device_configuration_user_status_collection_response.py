from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_configuration_user_status import DeviceConfigurationUserStatus


@dataclass
class DeviceConfigurationUserStatusCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceConfigurationUserStatus]
):
    value: Optional[List[DeviceConfigurationUserStatus]] = None

    def __init__(self):
        super().__init__(entity=DeviceConfigurationUserStatus)
