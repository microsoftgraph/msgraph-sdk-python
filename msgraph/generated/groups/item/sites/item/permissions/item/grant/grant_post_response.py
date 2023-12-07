from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ........models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ........models.permission import Permission


@dataclass
class GrantPostResponse(BaseCollectionPaginationCountResponse[Permission]):
    value: Optional[List[Permission]] = None

    def __init__(self):
        super().__init__(entity=Permission)
