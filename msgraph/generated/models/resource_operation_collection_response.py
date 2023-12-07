from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .resource_operation import ResourceOperation


@dataclass
class ResourceOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[ResourceOperation]
):
    value: Optional[List[ResourceOperation]] = None

    def __init__(self):
        super().__init__(entity=ResourceOperation)
