from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .browser_site import BrowserSite


@dataclass
class BrowserSiteCollectionResponse(BaseCollectionPaginationCountResponse[BrowserSite]):
    value: Optional[List[BrowserSite]] = None

    def __init__(self):
        super().__init__(entity=BrowserSite)
