from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .team import Team


@dataclass
class TeamCollectionResponse(BaseCollectionPaginationCountResponse[Team]):
    value: Optional[List[Team]] = None

    def __init__(self):
        super().__init__(entity=Team)
