from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .subdomain import Subdomain


@dataclass
class SubdomainCollectionResponse(BaseCollectionPaginationCountResponse[Subdomain]):
    value: Optional[List[Subdomain]] = None

    def __init__(self):
        super().__init__(entity=Subdomain)
