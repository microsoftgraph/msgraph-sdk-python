from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment


@dataclass
class DeviceAndAppManagementRoleAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceAndAppManagementRoleAssignment]
):
    value: Optional[List[DeviceAndAppManagementRoleAssignment]] = None

    def __init__(self):
        super().__init__(entity=DeviceAndAppManagementRoleAssignment)
