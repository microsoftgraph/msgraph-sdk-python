from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .drive_item_version import DriveItemVersion


@dataclass
class DriveItemVersionCollectionResponse(
    BaseCollectionPaginationCountResponse[DriveItemVersion]
):
    value: Optional[List[DriveItemVersion]] = None

    def __init__(self):
        super().__init__(entity=DriveItemVersion)
