from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .claims_mapping_policy import ClaimsMappingPolicy


@dataclass
class ClaimsMappingPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[ClaimsMappingPolicy]
):
    value: Optional[List[ClaimsMappingPolicy]] = None

    def __init__(self):
        super().__init__(entity=ClaimsMappingPolicy)
