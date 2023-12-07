from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .room import Room


@dataclass
class RoomCollectionResponse(BaseCollectionPaginationCountResponse[Room]):
    value: Optional[List[Room]] = None

    def __init__(self):
        super().__init__(entity=Room)
