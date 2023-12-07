from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .event import Event


@dataclass
class EventCollectionResponse(BaseCollectionPaginationCountResponse[Event]):
    value: Optional[List[Event]] = None

    def __init__(self):
        super().__init__(entity=Event)
