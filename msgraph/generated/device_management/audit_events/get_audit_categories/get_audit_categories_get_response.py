from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class GetAuditCategoriesGetResponse(BaseCollectionPaginationCountResponse[str]):
    value: Optional[List[str]] = None

    def __init__(self):
        super().__init__(entity=str)
