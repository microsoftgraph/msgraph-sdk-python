from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .intelligence_profile_indicator import IntelligenceProfileIndicator


@dataclass
class IntelligenceProfileIndicatorCollectionResponse(
    BaseCollectionPaginationCountResponse[IntelligenceProfileIndicator]
):
    value: Optional[List[IntelligenceProfileIndicator]] = None

    def __init__(self):
        super().__init__(entity=IntelligenceProfileIndicator)
