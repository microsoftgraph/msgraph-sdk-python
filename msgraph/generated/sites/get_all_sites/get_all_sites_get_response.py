from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ...models.site import Site


@dataclass
class GetAllSitesGetResponse(BaseCollectionPaginationCountResponse[Site]):
    value: Optional[List[Site]] = None

    def __init__(self):
        super().__init__(entity=Site)
