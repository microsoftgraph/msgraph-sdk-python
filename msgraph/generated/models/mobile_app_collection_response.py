from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mobile_app import MobileApp


@dataclass
class MobileAppCollectionResponse(BaseCollectionPaginationCountResponse[MobileApp]):
    value: Optional[List[MobileApp]] = None

    def __init__(self):
        super().__init__(entity=MobileApp)
