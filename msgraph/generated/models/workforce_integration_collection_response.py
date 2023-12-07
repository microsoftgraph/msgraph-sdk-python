from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workforce_integration import WorkforceIntegration


@dataclass
class WorkforceIntegrationCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkforceIntegration]
):
    value: Optional[List[WorkforceIntegration]] = None

    def __init__(self):
        super().__init__(entity=WorkforceIntegration)
