from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .custom_extension_stage_setting import CustomExtensionStageSetting


@dataclass
class CustomExtensionStageSettingCollectionResponse(
    BaseCollectionPaginationCountResponse[CustomExtensionStageSetting]
):
    value: Optional[List[CustomExtensionStageSetting]] = None

    def __init__(self):
        super().__init__(entity=CustomExtensionStageSetting)
