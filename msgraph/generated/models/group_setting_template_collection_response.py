from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .group_setting_template import GroupSettingTemplate


@dataclass
class GroupSettingTemplateCollectionResponse(
    BaseCollectionPaginationCountResponse[GroupSettingTemplate]
):
    value: Optional[List[GroupSettingTemplate]] = None

    def __init__(self):
        super().__init__(entity=GroupSettingTemplate)
