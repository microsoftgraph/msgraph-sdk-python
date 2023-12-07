from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_named_item import WorkbookNamedItem


@dataclass
class WorkbookNamedItemCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookNamedItem]
):
    value: Optional[List[WorkbookNamedItem]] = None

    def __init__(self):
        super().__init__(entity=WorkbookNamedItem)
