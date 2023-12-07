from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .print_document import PrintDocument


@dataclass
class PrintDocumentCollectionResponse(
    BaseCollectionPaginationCountResponse[PrintDocument]
):
    value: Optional[List[PrintDocument]] = None

    def __init__(self):
        super().__init__(entity=PrintDocument)
