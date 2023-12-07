from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_app_policy import ManagedAppPolicy


@dataclass
class ManagedAppPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[ManagedAppPolicy]
):
    value: Optional[List[ManagedAppPolicy]] = None

    def __init__(self):
        super().__init__(entity=ManagedAppPolicy)
