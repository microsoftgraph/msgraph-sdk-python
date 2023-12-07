from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.imported_windows_autopilot_device_identity import (
    ImportedWindowsAutopilotDeviceIdentity,
)


@dataclass
class ImportPostResponse(
    BaseCollectionPaginationCountResponse[ImportedWindowsAutopilotDeviceIdentity]
):
    value: Optional[List[ImportedWindowsAutopilotDeviceIdentity]] = None

    def __init__(self):
        super().__init__(entity=ImportedWindowsAutopilotDeviceIdentity)
