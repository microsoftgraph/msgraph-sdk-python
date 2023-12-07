from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .host_tracker import HostTracker


@dataclass
class HostTrackerCollectionResponse(BaseCollectionPaginationCountResponse[HostTracker]):
    value: Optional[List[HostTracker]] = None

    def __init__(self):
        super().__init__(entity=HostTracker)
