from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .shared_drive_item import SharedDriveItem


@dataclass
class SharedDriveItemCollectionResponse(
    BaseCollectionPaginationCountResponse[SharedDriveItem]
):
    value: Optional[List[SharedDriveItem]] = None

    def __init__(self):
        super().__init__(entity=SharedDriveItem)
