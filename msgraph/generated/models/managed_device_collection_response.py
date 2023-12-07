from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_device import ManagedDevice


@dataclass
class ManagedDeviceCollectionResponse(
    BaseCollectionPaginationCountResponse[ManagedDevice]
):
    value: Optional[List[ManagedDevice]] = None

    def __init__(self):
        super().__init__(entity=ManagedDevice)
