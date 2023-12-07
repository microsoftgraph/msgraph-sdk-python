from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ......models.base_delta_function_response import BaseDeltaFunctionResponse
from ......models.drive_item import DriveItem


@dataclass
class DeltaWithTokenGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[DriveItem]] = None

    def __init__(self):
        super().__init__(entity=DriveItem)
