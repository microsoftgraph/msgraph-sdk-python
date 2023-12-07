from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .used_insight import UsedInsight


@dataclass
class UsedInsightCollectionResponse(BaseCollectionPaginationCountResponse[UsedInsight]):
    value: Optional[List[UsedInsight]] = None

    def __init__(self):
        super().__init__(entity=UsedInsight)
