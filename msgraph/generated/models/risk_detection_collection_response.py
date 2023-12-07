from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .risk_detection import RiskDetection


@dataclass
class RiskDetectionCollectionResponse(
    BaseCollectionPaginationCountResponse[RiskDetection]
):
    value: Optional[List[RiskDetection]] = None

    def __init__(self):
        super().__init__(entity=RiskDetection)
