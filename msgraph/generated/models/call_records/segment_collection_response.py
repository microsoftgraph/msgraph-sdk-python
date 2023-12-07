from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .segment import Segment


@dataclass
class SegmentCollectionResponse(BaseCollectionPaginationCountResponse[Segment]):
    value: Optional[List[Segment]] = None

    def __init__(self):
        super().__init__(entity=Segment)
