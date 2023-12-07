from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .shared_with_channel_team_info import SharedWithChannelTeamInfo


@dataclass
class SharedWithChannelTeamInfoCollectionResponse(
    BaseCollectionPaginationCountResponse[SharedWithChannelTeamInfo]
):
    value: Optional[List[SharedWithChannelTeamInfo]] = None

    def __init__(self):
        super().__init__(entity=SharedWithChannelTeamInfo)
