from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package_resource_role import AccessPackageResourceRole
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageResourceRoleCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackageResourceRole]
):
    value: Optional[List[AccessPackageResourceRole]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageResourceRole)
