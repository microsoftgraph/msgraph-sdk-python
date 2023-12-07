from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .list_item_version import ListItemVersion


@dataclass
class ListItemVersionCollectionResponse(
    BaseCollectionPaginationCountResponse[ListItemVersion]
):
    value: Optional[List[ListItemVersion]] = None

    def __init__(self):
        super().__init__(entity=ListItemVersion)
