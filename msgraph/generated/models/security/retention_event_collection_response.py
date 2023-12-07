from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .retention_event import RetentionEvent


@dataclass
class RetentionEventCollectionResponse(
    BaseCollectionPaginationCountResponse[RetentionEvent]
):
    value: Optional[List[RetentionEvent]] = None

    def __init__(self):
        super().__init__(entity=RetentionEvent)
