from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .long_running_operation import LongRunningOperation


@dataclass
class LongRunningOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[LongRunningOperation]
):
    value: Optional[List[LongRunningOperation]] = None

    def __init__(self):
        super().__init__(entity=LongRunningOperation)
