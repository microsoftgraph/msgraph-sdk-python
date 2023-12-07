from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .outlook_category import OutlookCategory


@dataclass
class OutlookCategoryCollectionResponse(
    BaseCollectionPaginationCountResponse[OutlookCategory]
):
    value: Optional[List[OutlookCategory]] = None

    def __init__(self):
        super().__init__(entity=OutlookCategory)
