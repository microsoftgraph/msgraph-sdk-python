from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .app_log_collection_request import AppLogCollectionRequest
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AppLogCollectionRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[AppLogCollectionRequest]
):
    value: Optional[List[AppLogCollectionRequest]] = None

    def __init__(self):
        super().__init__(entity=AppLogCollectionRequest)
