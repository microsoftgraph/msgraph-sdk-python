from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .role_definition import RoleDefinition


@dataclass
class RoleDefinitionCollectionResponse(
    BaseCollectionPaginationCountResponse[RoleDefinition]
):
    value: Optional[List[RoleDefinition]] = None

    def __init__(self):
        super().__init__(entity=RoleDefinition)
