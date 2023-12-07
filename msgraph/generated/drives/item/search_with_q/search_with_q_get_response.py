from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.drive_item import DriveItem


@dataclass
class SearchWithQGetResponse(BaseCollectionPaginationCountResponse[DriveItem]):
    value: Optional[List[DriveItem]] = None

    def __init__(self):
        super().__init__(entity=DriveItem)
