from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.resource_specific_permission_grant import ResourceSpecificPermissionGrant


@dataclass
class CheckGrantedPermissionsForAppPostResponse(
    BaseCollectionPaginationCountResponse[ResourceSpecificPermissionGrant]
):
    value: Optional[List[ResourceSpecificPermissionGrant]] = None

    def __init__(self):
        super().__init__(entity=ResourceSpecificPermissionGrant)
