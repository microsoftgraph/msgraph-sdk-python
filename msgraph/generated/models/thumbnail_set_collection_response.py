from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .thumbnail_set import ThumbnailSet


@dataclass
class ThumbnailSetCollectionResponse(
    BaseCollectionPaginationCountResponse[ThumbnailSet]
):
    value: Optional[List[ThumbnailSet]] = None

    def __init__(self):
        super().__init__(entity=ThumbnailSet)
