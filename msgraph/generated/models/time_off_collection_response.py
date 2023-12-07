from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .time_off import TimeOff


@dataclass
class TimeOffCollectionResponse(BaseCollectionPaginationCountResponse[TimeOff]):
    value: Optional[List[TimeOff]] = None

    def __init__(self):
        super().__init__(entity=TimeOff)
