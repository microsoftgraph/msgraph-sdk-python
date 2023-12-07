from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .rich_long_running_operation import RichLongRunningOperation


@dataclass
class RichLongRunningOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[RichLongRunningOperation]
):
    value: Optional[List[RichLongRunningOperation]] = None

    def __init__(self):
        super().__init__(entity=RichLongRunningOperation)
