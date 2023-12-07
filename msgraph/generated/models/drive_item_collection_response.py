from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .drive_item import DriveItem


@dataclass
class DriveItemCollectionResponse(BaseCollectionPaginationCountResponse[DriveItem]):
    value: Optional[List[DriveItem]] = None

    def __init__(self):
        super().__init__(entity=DriveItem)
