from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .online_meeting import OnlineMeeting


@dataclass
class OnlineMeetingCollectionResponse(
    BaseCollectionPaginationCountResponse[OnlineMeeting]
):
    value: Optional[List[OnlineMeeting]] = None

    def __init__(self):
        super().__init__(entity=OnlineMeeting)
