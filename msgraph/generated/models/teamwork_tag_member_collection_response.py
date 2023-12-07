from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .teamwork_tag_member import TeamworkTagMember


@dataclass
class TeamworkTagMemberCollectionResponse(
    BaseCollectionPaginationCountResponse[TeamworkTagMember]
):
    value: Optional[List[TeamworkTagMember]] = None

    def __init__(self):
        super().__init__(entity=TeamworkTagMember)
