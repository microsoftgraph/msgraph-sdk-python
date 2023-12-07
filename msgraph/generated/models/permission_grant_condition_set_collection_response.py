from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .permission_grant_condition_set import PermissionGrantConditionSet


@dataclass
class PermissionGrantConditionSetCollectionResponse(
    BaseCollectionPaginationCountResponse[PermissionGrantConditionSet]
):
    value: Optional[List[PermissionGrantConditionSet]] = None

    def __init__(self):
        super().__init__(entity=PermissionGrantConditionSet)
