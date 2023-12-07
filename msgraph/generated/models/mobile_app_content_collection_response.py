from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mobile_app_content import MobileAppContent


@dataclass
class MobileAppContentCollectionResponse(
    BaseCollectionPaginationCountResponse[MobileAppContent]
):
    value: Optional[List[MobileAppContent]] = None

    def __init__(self):
        super().__init__(entity=MobileAppContent)
