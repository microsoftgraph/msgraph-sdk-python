from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .group_lifecycle_policy import GroupLifecyclePolicy


@dataclass
class GroupLifecyclePolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[GroupLifecyclePolicy]
):
    value: Optional[List[GroupLifecyclePolicy]] = None

    def __init__(self):
        super().__init__(entity=GroupLifecyclePolicy)
