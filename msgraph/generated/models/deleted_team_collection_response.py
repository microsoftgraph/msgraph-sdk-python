from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .deleted_team import DeletedTeam


@dataclass
class DeletedTeamCollectionResponse(BaseCollectionPaginationCountResponse[DeletedTeam]):
    value: Optional[List[DeletedTeam]] = None

    def __init__(self):
        super().__init__(entity=DeletedTeam)
