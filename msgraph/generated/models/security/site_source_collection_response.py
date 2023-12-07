from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .site_source import SiteSource


@dataclass
class SiteSourceCollectionResponse(BaseCollectionPaginationCountResponse[SiteSource]):
    value: Optional[List[SiteSource]] = None

    def __init__(self):
        super().__init__(entity=SiteSource)
