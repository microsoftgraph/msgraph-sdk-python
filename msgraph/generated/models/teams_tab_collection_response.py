from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .teams_tab import TeamsTab


@dataclass
class TeamsTabCollectionResponse(BaseCollectionPaginationCountResponse[TeamsTab]):
    value: Optional[List[TeamsTab]] = None

    def __init__(self):
        super().__init__(entity=TeamsTab)
