from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent


@dataclass
class DeviceManagementTroubleshootingEventCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceManagementTroubleshootingEvent]
):
    value: Optional[List[DeviceManagementTroubleshootingEvent]] = None

    def __init__(self):
        super().__init__(entity=DeviceManagementTroubleshootingEvent)
