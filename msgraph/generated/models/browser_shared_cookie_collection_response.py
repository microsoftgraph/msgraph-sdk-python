from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .browser_shared_cookie import BrowserSharedCookie


@dataclass
class BrowserSharedCookieCollectionResponse(
    BaseCollectionPaginationCountResponse[BrowserSharedCookie]
):
    value: Optional[List[BrowserSharedCookie]] = None

    def __init__(self):
        super().__init__(entity=BrowserSharedCookie)
