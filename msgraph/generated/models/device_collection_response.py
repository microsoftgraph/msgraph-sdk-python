from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device import Device


@dataclass
class DeviceCollectionResponse(BaseCollectionPaginationCountResponse[Device]):
    value: Optional[List[Device]] = None

    def __init__(self):
        super().__init__(entity=Device)
