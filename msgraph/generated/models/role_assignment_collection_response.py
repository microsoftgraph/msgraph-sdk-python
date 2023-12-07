from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .role_assignment import RoleAssignment


@dataclass
class RoleAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[RoleAssignment]
):
    value: Optional[List[RoleAssignment]] = None

    def __init__(self):
        super().__init__(entity=RoleAssignment)
