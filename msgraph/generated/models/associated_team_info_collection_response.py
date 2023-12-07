from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .associated_team_info import AssociatedTeamInfo
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AssociatedTeamInfoCollectionResponse(
    BaseCollectionPaginationCountResponse[AssociatedTeamInfo]
):
    value: Optional[List[AssociatedTeamInfo]] = None

    def __init__(self):
        super().__init__(entity=AssociatedTeamInfo)
