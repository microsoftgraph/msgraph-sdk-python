from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .subscribed_sku import SubscribedSku


@dataclass
class SubscribedSkuCollectionResponse(
    BaseCollectionPaginationCountResponse[SubscribedSku]
):
    value: Optional[List[SubscribedSku]] = None

    def __init__(self):
        super().__init__(entity=SubscribedSku)
