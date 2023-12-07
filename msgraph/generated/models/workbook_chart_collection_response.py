from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_chart import WorkbookChart


@dataclass
class WorkbookChartCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookChart]
):
    value: Optional[List[WorkbookChart]] = None

    def __init__(self):
        super().__init__(entity=WorkbookChart)
