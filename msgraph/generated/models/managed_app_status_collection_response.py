from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_app_status import ManagedAppStatus


@dataclass
class ManagedAppStatusCollectionResponse(
    BaseCollectionPaginationCountResponse[ManagedAppStatus]
):
    value: Optional[List[ManagedAppStatus]] = None

    def __init__(self):
        super().__init__(entity=ManagedAppStatus)
