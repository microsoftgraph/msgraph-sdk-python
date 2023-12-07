from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .threat_assessment_result import ThreatAssessmentResult


@dataclass
class ThreatAssessmentResultCollectionResponse(
    BaseCollectionPaginationCountResponse[ThreatAssessmentResult]
):
    value: Optional[List[ThreatAssessmentResult]] = None

    def __init__(self):
        super().__init__(entity=ThreatAssessmentResult)
