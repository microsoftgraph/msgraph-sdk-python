from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .unified_rbac_resource_action import UnifiedRbacResourceAction


@dataclass
class UnifiedRbacResourceActionCollectionResponse(
    BaseCollectionPaginationCountResponse[UnifiedRbacResourceAction]
):
    value: Optional[List[UnifiedRbacResourceAction]] = None

    def __init__(self):
        super().__init__(entity=UnifiedRbacResourceAction)
