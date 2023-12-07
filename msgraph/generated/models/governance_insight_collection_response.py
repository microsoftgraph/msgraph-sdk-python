from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .governance_insight import GovernanceInsight


@dataclass
class GovernanceInsightCollectionResponse(
    BaseCollectionPaginationCountResponse[GovernanceInsight]
):
    value: Optional[List[GovernanceInsight]] = None

    def __init__(self):
        super().__init__(entity=GovernanceInsight)
