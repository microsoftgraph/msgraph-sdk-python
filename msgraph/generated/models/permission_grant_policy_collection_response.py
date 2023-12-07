from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .permission_grant_policy import PermissionGrantPolicy


@dataclass
class PermissionGrantPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[PermissionGrantPolicy]
):
    value: Optional[List[PermissionGrantPolicy]] = None

    def __init__(self):
        super().__init__(entity=PermissionGrantPolicy)
