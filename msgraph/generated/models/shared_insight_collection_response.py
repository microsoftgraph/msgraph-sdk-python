from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .shared_insight import SharedInsight


@dataclass
class SharedInsightCollectionResponse(
    BaseCollectionPaginationCountResponse[SharedInsight]
):
    value: Optional[List[SharedInsight]] = None

    def __init__(self):
        super().__init__(entity=SharedInsight)
