from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .printer_share import PrinterShare


@dataclass
class PrinterShareCollectionResponse(
    BaseCollectionPaginationCountResponse[PrinterShare]
):
    value: Optional[List[PrinterShare]] = None

    def __init__(self):
        super().__init__(entity=PrinterShare)
