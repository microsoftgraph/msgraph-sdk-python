from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_pivot_table import WorkbookPivotTable


@dataclass
class WorkbookPivotTableCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookPivotTable]
):
    value: Optional[List[WorkbookPivotTable]] = None

    def __init__(self):
        super().__init__(entity=WorkbookPivotTable)
