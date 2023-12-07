from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_chart_point import WorkbookChartPoint


@dataclass
class WorkbookChartPointCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookChartPoint]
):
    value: Optional[List[WorkbookChartPoint]] = None

    def __init__(self):
        super().__init__(entity=WorkbookChartPoint)
