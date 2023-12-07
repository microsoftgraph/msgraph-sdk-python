from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_device_mobile_app_configuration_user_status import (
    ManagedDeviceMobileAppConfigurationUserStatus,
)


@dataclass
class ManagedDeviceMobileAppConfigurationUserStatusCollectionResponse(
    BaseCollectionPaginationCountResponse[ManagedDeviceMobileAppConfigurationUserStatus]
):
    value: Optional[List[ManagedDeviceMobileAppConfigurationUserStatus]] = None

    def __init__(self):
        super().__init__(entity=ManagedDeviceMobileAppConfigurationUserStatus)
