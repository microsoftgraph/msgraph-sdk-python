from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .comms_operation import CommsOperation


@dataclass
class CommsOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[CommsOperation]
):
    value: Optional[List[CommsOperation]] = None

    def __init__(self):
        super().__init__(entity=CommsOperation)
