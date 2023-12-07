from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .audio_routing_group import AudioRoutingGroup
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AudioRoutingGroupCollectionResponse(
    BaseCollectionPaginationCountResponse[AudioRoutingGroup]
):
    value: Optional[List[AudioRoutingGroup]] = None

    def __init__(self):
        super().__init__(entity=AudioRoutingGroup)
