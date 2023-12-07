from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .service_health import ServiceHealth


@dataclass
class ServiceHealthCollectionResponse(
    BaseCollectionPaginationCountResponse[ServiceHealth]
):
    value: Optional[List[ServiceHealth]] = None

    def __init__(self):
        super().__init__(entity=ServiceHealth)
