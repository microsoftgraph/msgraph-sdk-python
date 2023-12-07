from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem


@dataclass
class RiskyServicePrincipalHistoryItemCollectionResponse(
    BaseCollectionPaginationCountResponse[RiskyServicePrincipalHistoryItem]
):
    value: Optional[List[RiskyServicePrincipalHistoryItem]] = None

    def __init__(self):
        super().__init__(entity=RiskyServicePrincipalHistoryItem)
