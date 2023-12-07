from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .presence import Presence


@dataclass
class PresenceCollectionResponse(BaseCollectionPaginationCountResponse[Presence]):
    value: Optional[List[Presence]] = None

    def __init__(self):
        super().__init__(entity=Presence)
