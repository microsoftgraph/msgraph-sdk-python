from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .browser_site_list import BrowserSiteList


@dataclass
class BrowserSiteListCollectionResponse(
    BaseCollectionPaginationCountResponse[BrowserSiteList]
):
    value: Optional[List[BrowserSiteList]] = None

    def __init__(self):
        super().__init__(entity=BrowserSiteList)
