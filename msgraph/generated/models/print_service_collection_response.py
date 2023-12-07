from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .print_service import PrintService


@dataclass
class PrintServiceCollectionResponse(
    BaseCollectionPaginationCountResponse[PrintService]
):
    value: Optional[List[PrintService]] = None

    def __init__(self):
        super().__init__(entity=PrintService)
