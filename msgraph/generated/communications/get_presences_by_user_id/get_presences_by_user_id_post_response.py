from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ...models.presence import Presence


@dataclass
class GetPresencesByUserIdPostResponse(BaseCollectionPaginationCountResponse[Presence]):
    value: Optional[List[Presence]] = None

    def __init__(self):
        super().__init__(entity=Presence)
