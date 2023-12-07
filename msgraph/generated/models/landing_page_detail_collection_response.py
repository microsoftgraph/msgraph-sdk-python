from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .landing_page_detail import LandingPageDetail


@dataclass
class LandingPageDetailCollectionResponse(
    BaseCollectionPaginationCountResponse[LandingPageDetail]
):
    value: Optional[List[LandingPageDetail]] = None

    def __init__(self):
        super().__init__(entity=LandingPageDetail)
