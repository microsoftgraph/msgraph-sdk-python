from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .app_management_policy import AppManagementPolicy
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AppManagementPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[AppManagementPolicy]
):
    value: Optional[List[AppManagementPolicy]] = None

    def __init__(self):
        super().__init__(entity=AppManagementPolicy)
