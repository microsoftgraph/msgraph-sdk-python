from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .delegated_permission_classification import DelegatedPermissionClassification


@dataclass
class DelegatedPermissionClassificationCollectionResponse(
    BaseCollectionPaginationCountResponse[DelegatedPermissionClassification]
):
    value: Optional[List[DelegatedPermissionClassification]] = None

    def __init__(self):
        super().__init__(entity=DelegatedPermissionClassification)
