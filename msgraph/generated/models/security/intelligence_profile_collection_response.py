from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .intelligence_profile import IntelligenceProfile


@dataclass
class IntelligenceProfileCollectionResponse(
    BaseCollectionPaginationCountResponse[IntelligenceProfile]
):
    value: Optional[List[IntelligenceProfile]] = None

    def __init__(self):
        super().__init__(entity=IntelligenceProfile)
