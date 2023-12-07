from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class ActivityBasedTimeoutPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[ActivityBasedTimeoutPolicy]
):
    value: Optional[List[ActivityBasedTimeoutPolicy]] = None

    def __init__(self):
        super().__init__(entity=ActivityBasedTimeoutPolicy)
