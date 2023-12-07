from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .time_off_reason import TimeOffReason


@dataclass
class TimeOffReasonCollectionResponse(
    BaseCollectionPaginationCountResponse[TimeOffReason]
):
    value: Optional[List[TimeOffReason]] = None

    def __init__(self):
        super().__init__(entity=TimeOffReason)
