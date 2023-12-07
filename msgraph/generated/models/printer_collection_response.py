from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .printer import Printer


@dataclass
class PrinterCollectionResponse(BaseCollectionPaginationCountResponse[Printer]):
    value: Optional[List[Printer]] = None

    def __init__(self):
        super().__init__(entity=Printer)
