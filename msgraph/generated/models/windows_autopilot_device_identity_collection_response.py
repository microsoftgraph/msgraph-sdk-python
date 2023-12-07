from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity


@dataclass
class WindowsAutopilotDeviceIdentityCollectionResponse(
    BaseCollectionPaginationCountResponse[WindowsAutopilotDeviceIdentity]
):
    value: Optional[List[WindowsAutopilotDeviceIdentity]] = None

    def __init__(self):
        super().__init__(entity=WindowsAutopilotDeviceIdentity)
