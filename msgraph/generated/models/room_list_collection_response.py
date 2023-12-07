from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .room_list import RoomList


@dataclass
class RoomListCollectionResponse(BaseCollectionPaginationCountResponse[RoomList]):
    value: Optional[List[RoomList]] = None

    def __init__(self):
        super().__init__(entity=RoomList)
