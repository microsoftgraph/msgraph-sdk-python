from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .token_lifetime_policy import TokenLifetimePolicy


@dataclass
class TokenLifetimePolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[TokenLifetimePolicy]
):
    value: Optional[List[TokenLifetimePolicy]] = None

    def __init__(self):
        super().__init__(entity=TokenLifetimePolicy)
