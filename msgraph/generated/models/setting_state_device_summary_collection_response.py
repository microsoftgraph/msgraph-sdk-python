from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .setting_state_device_summary import SettingStateDeviceSummary


@dataclass
class SettingStateDeviceSummaryCollectionResponse(
    BaseCollectionPaginationCountResponse[SettingStateDeviceSummary]
):
    value: Optional[List[SettingStateDeviceSummary]] = None

    def __init__(self):
        super().__init__(entity=SettingStateDeviceSummary)
