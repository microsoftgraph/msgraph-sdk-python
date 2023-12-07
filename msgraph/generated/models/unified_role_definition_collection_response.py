from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .unified_role_definition import UnifiedRoleDefinition


@dataclass
class UnifiedRoleDefinitionCollectionResponse(
    BaseCollectionPaginationCountResponse[UnifiedRoleDefinition]
):
    value: Optional[List[UnifiedRoleDefinition]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRoleDefinition)
