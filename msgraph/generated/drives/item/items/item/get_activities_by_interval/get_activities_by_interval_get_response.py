from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ......models.item_activity_stat import ItemActivityStat


@dataclass
class GetActivitiesByIntervalGetResponse(
    BaseCollectionPaginationCountResponse[ItemActivityStat]
):
    value: Optional[List[ItemActivityStat]] = None

    def __init__(self):
        super().__init__(entity=ItemActivityStat)
