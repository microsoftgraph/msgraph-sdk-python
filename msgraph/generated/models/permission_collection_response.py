from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .permission import Permission


@dataclass
class PermissionCollectionResponse(BaseCollectionPaginationCountResponse[Permission]):
    value: Optional[List[Permission]] = None

    def __init__(self):
        super().__init__(entity=Permission)
