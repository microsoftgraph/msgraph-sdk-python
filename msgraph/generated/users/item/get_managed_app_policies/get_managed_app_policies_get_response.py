from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.managed_app_policy import ManagedAppPolicy


@dataclass
class GetManagedAppPoliciesGetResponse(
    BaseCollectionPaginationCountResponse[ManagedAppPolicy]
):
    value: Optional[List[ManagedAppPolicy]] = None

    def __init__(self):
        super().__init__(entity=ManagedAppPolicy)
