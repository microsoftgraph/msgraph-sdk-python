from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .print_usage_by_user import PrintUsageByUser


@dataclass
class PrintUsageByUserCollectionResponse(
    BaseCollectionPaginationCountResponse[PrintUsageByUser]
):
    value: Optional[List[PrintUsageByUser]] = None

    def __init__(self):
        super().__init__(entity=PrintUsageByUser)
