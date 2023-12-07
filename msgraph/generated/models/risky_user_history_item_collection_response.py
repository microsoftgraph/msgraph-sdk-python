from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .risky_user_history_item import RiskyUserHistoryItem


@dataclass
class RiskyUserHistoryItemCollectionResponse(
    BaseCollectionPaginationCountResponse[RiskyUserHistoryItem]
):
    value: Optional[List[RiskyUserHistoryItem]] = None

    def __init__(self):
        super().__init__(entity=RiskyUserHistoryItem)
