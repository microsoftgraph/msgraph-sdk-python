from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .....models.device_configuration_assignment import DeviceConfigurationAssignment


@dataclass
class AssignPostResponse(
    BaseCollectionPaginationCountResponse[DeviceConfigurationAssignment]
):
    value: Optional[List[DeviceConfigurationAssignment]] = None

    def __init__(self):
        super().__init__(entity=DeviceConfigurationAssignment)
