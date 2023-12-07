from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .host_cookie import HostCookie


@dataclass
class HostCookieCollectionResponse(BaseCollectionPaginationCountResponse[HostCookie]):
    value: Optional[List[HostCookie]] = None

    def __init__(self):
        super().__init__(entity=HostCookie)
