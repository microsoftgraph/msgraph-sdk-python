from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .landing_page import LandingPage


@dataclass
class LandingPageCollectionResponse(BaseCollectionPaginationCountResponse[LandingPage]):
    value: Optional[List[LandingPage]] = None

    def __init__(self):
        super().__init__(entity=LandingPage)
