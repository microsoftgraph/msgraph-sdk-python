from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment


@dataclass
class DelegatedAdminAccessAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[DelegatedAdminAccessAssignment]
):
    value: Optional[List[DelegatedAdminAccessAssignment]] = None

    def __init__(self):
        super().__init__(entity=DelegatedAdminAccessAssignment)
