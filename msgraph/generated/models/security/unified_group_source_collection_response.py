from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .unified_group_source import UnifiedGroupSource


@dataclass
class UnifiedGroupSourceCollectionResponse(
    BaseCollectionPaginationCountResponse[UnifiedGroupSource]
):
    value: Optional[List[UnifiedGroupSource]] = None

    def __init__(self):
        super().__init__(entity=UnifiedGroupSource)
