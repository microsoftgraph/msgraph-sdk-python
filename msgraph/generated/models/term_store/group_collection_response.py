from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .group import Group


@dataclass
class GroupCollectionResponse(BaseCollectionPaginationCountResponse[Group]):
    value: Optional[List[Group]] = None

    def __init__(self):
        super().__init__(entity=Group)
