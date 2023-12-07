from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .service_health_issue import ServiceHealthIssue


@dataclass
class ServiceHealthIssueCollectionResponse(
    BaseCollectionPaginationCountResponse[ServiceHealthIssue]
):
    value: Optional[List[ServiceHealthIssue]] = None

    def __init__(self):
        super().__init__(entity=ServiceHealthIssue)
