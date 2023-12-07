from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_configuration import DeviceConfiguration


@dataclass
class DeviceConfigurationCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceConfiguration]
):
    value: Optional[List[DeviceConfiguration]] = None

    def __init__(self):
        super().__init__(entity=DeviceConfiguration)
