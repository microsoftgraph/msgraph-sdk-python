from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity


@dataclass
class ImportedWindowsAutopilotDeviceIdentityCollectionResponse(
    BaseCollectionPaginationCountResponse[ImportedWindowsAutopilotDeviceIdentity]
):
    value: Optional[List[ImportedWindowsAutopilotDeviceIdentity]] = None

    def __init__(self):
        super().__init__(entity=ImportedWindowsAutopilotDeviceIdentity)
