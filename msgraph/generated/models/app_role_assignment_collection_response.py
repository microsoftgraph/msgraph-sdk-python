from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .app_role_assignment import AppRoleAssignment
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AppRoleAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[AppRoleAssignment]
):
    value: Optional[List[AppRoleAssignment]] = None

    def __init__(self):
        super().__init__(entity=AppRoleAssignment)
