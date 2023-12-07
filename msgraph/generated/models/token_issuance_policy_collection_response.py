from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .token_issuance_policy import TokenIssuancePolicy


@dataclass
class TokenIssuancePolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[TokenIssuancePolicy]
):
    value: Optional[List[TokenIssuancePolicy]] = None

    def __init__(self):
        super().__init__(entity=TokenIssuancePolicy)
