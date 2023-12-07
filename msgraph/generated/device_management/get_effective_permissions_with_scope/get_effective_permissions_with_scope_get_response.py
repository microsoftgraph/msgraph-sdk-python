from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ...models.role_permission import RolePermission


@dataclass
class GetEffectivePermissionsWithScopeGetResponse(
    BaseCollectionPaginationCountResponse[RolePermission]
):
    value: Optional[List[RolePermission]] = None

    def __init__(self):
        super().__init__(entity=RolePermission)
