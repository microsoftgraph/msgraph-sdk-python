from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_management_export_job import DeviceManagementExportJob


@dataclass
class DeviceManagementExportJobCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceManagementExportJob]
):
    value: Optional[List[DeviceManagementExportJob]] = None

    def __init__(self):
        super().__init__(entity=DeviceManagementExportJob)
