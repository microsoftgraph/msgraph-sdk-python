from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .service_principal_risk_detection import ServicePrincipalRiskDetection


@dataclass
class ServicePrincipalRiskDetectionCollectionResponse(
    BaseCollectionPaginationCountResponse[ServicePrincipalRiskDetection]
):
    value: Optional[List[ServicePrincipalRiskDetection]] = None

    def __init__(self):
        super().__init__(entity=ServicePrincipalRiskDetection)
