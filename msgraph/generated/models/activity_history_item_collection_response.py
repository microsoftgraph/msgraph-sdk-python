from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .activity_history_item import ActivityHistoryItem
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class ActivityHistoryItemCollectionResponse(
    BaseCollectionPaginationCountResponse[ActivityHistoryItem]
):
    value: Optional[List[ActivityHistoryItem]] = None

    def __init__(self):
        super().__init__(entity=ActivityHistoryItem)
