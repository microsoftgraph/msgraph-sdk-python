from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .subscription import Subscription


@dataclass
class SubscriptionCollectionResponse(
    BaseCollectionPaginationCountResponse[Subscription]
):
    value: Optional[List[Subscription]] = None

    def __init__(self):
        super().__init__(entity=Subscription)
