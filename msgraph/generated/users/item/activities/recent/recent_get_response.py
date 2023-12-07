from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .....models.user_activity import UserActivity


@dataclass
class RecentGetResponse(BaseCollectionPaginationCountResponse[UserActivity]):
    value: Optional[List[UserActivity]] = None

    def __init__(self):
        super().__init__(entity=UserActivity)
