from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .teams_async_operation import TeamsAsyncOperation


@dataclass
class TeamsAsyncOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[TeamsAsyncOperation]
):
    value: Optional[List[TeamsAsyncOperation]] = None

    def __init__(self):
        super().__init__(entity=TeamsAsyncOperation)
