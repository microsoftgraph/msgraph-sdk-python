from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .list_item import ListItem


@dataclass
class ListItemCollectionResponse(BaseCollectionPaginationCountResponse[ListItem]):
    value: Optional[List[ListItem]] = None

    def __init__(self):
        super().__init__(entity=ListItem)
