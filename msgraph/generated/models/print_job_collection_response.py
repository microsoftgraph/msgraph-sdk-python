from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .print_job import PrintJob


@dataclass
class PrintJobCollectionResponse(BaseCollectionPaginationCountResponse[PrintJob]):
    value: Optional[List[PrintJob]] = None

    def __init__(self):
        super().__init__(entity=PrintJob)
