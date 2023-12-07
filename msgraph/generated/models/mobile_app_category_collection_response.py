from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mobile_app_category import MobileAppCategory


@dataclass
class MobileAppCategoryCollectionResponse(
    BaseCollectionPaginationCountResponse[MobileAppCategory]
):
    value: Optional[List[MobileAppCategory]] = None

    def __init__(self):
        super().__init__(entity=MobileAppCategory)
