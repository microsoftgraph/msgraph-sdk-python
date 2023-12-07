from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .conditional_access_policy import ConditionalAccessPolicy


@dataclass
class ConditionalAccessPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[ConditionalAccessPolicy]
):
    value: Optional[List[ConditionalAccessPolicy]] = None

    def __init__(self):
        super().__init__(entity=ConditionalAccessPolicy)
