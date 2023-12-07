from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .threat_assessment_request import ThreatAssessmentRequest


@dataclass
class ThreatAssessmentRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[ThreatAssessmentRequest]
):
    value: Optional[List[ThreatAssessmentRequest]] = None

    def __init__(self):
        super().__init__(entity=ThreatAssessmentRequest)
