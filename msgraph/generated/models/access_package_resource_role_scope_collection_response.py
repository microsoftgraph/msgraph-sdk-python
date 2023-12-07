from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package_resource_role_scope import AccessPackageResourceRoleScope
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageResourceRoleScopeCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackageResourceRoleScope]
):
    value: Optional[List[AccessPackageResourceRoleScope]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageResourceRoleScope)
