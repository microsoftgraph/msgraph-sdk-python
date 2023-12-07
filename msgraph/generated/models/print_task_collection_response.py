from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .print_task import PrintTask


@dataclass
class PrintTaskCollectionResponse(BaseCollectionPaginationCountResponse[PrintTask]):
    value: Optional[List[PrintTask]] = None

    def __init__(self):
        super().__init__(entity=PrintTask)
