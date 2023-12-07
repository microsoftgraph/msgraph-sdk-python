from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .column_link import ColumnLink


@dataclass
class ColumnLinkCollectionResponse(BaseCollectionPaginationCountResponse[ColumnLink]):
    value: Optional[List[ColumnLink]] = None

    def __init__(self):
        super().__init__(entity=ColumnLink)
