from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_activity import UserActivity


@dataclass
class UserActivityCollectionResponse(
    BaseCollectionPaginationCountResponse[UserActivity]
):
    value: Optional[List[UserActivity]] = None

    def __init__(self):
        super().__init__(entity=UserActivity)
