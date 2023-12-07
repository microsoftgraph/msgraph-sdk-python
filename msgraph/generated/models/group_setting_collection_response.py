from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .group_setting import GroupSetting


@dataclass
class GroupSettingCollectionResponse(
    BaseCollectionPaginationCountResponse[GroupSetting]
):
    value: Optional[List[GroupSetting]] = None

    def __init__(self):
        super().__init__(entity=GroupSetting)
