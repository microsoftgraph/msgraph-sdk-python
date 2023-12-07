from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_enrollment_configuration import DeviceEnrollmentConfiguration


@dataclass
class DeviceEnrollmentConfigurationCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceEnrollmentConfiguration]
):
    value: Optional[List[DeviceEnrollmentConfiguration]] = None

    def __init__(self):
        super().__init__(entity=DeviceEnrollmentConfiguration)
