from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .print_operation import PrintOperation


@dataclass
class PrintOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[PrintOperation]
):
    value: Optional[List[PrintOperation]] = None

    def __init__(self):
        super().__init__(entity=PrintOperation)
