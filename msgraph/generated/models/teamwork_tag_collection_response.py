from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .teamwork_tag import TeamworkTag


@dataclass
class TeamworkTagCollectionResponse(BaseCollectionPaginationCountResponse[TeamworkTag]):
    value: Optional[List[TeamworkTag]] = None

    def __init__(self):
        super().__init__(entity=TeamworkTag)
