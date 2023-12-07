from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ......models.recent_notebook import RecentNotebook


@dataclass
class GetRecentNotebooksWithIncludePersonalNotebooksGetResponse(
    BaseCollectionPaginationCountResponse[RecentNotebook]
):
    value: Optional[List[RecentNotebook]] = None

    def __init__(self):
        super().__init__(entity=RecentNotebook)
