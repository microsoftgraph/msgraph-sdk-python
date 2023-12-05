from __future__ import annotations

from dataclasses import dataclass

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .site import Site


@dataclass
class SitePagesCollectionResponse(BaseCollectionPaginationCountResponse[Site]):
    def __init__(self):
        super().__init__(entity=Site)
