from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_table import WorkbookTable


@dataclass
class WorkbookTableCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookTable]
):
    value: Optional[List[WorkbookTable]] = None

    def __init__(self):
        super().__init__(entity=WorkbookTable)
