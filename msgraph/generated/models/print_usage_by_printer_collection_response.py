from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .print_usage_by_printer import PrintUsageByPrinter


@dataclass
class PrintUsageByPrinterCollectionResponse(
    BaseCollectionPaginationCountResponse[PrintUsageByPrinter]
):
    value: Optional[List[PrintUsageByPrinter]] = None

    def __init__(self):
        super().__init__(entity=PrintUsageByPrinter)
