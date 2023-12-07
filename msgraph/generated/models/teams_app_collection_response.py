from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .teams_app import TeamsApp


@dataclass
class TeamsAppCollectionResponse(BaseCollectionPaginationCountResponse[TeamsApp]):
    value: Optional[List[TeamsApp]] = None

    def __init__(self):
        super().__init__(entity=TeamsApp)
