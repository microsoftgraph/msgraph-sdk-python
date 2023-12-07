from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_chart_series import WorkbookChartSeries


@dataclass
class WorkbookChartSeriesCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookChartSeries]
):
    value: Optional[List[WorkbookChartSeries]] = None

    def __init__(self):
        super().__init__(entity=WorkbookChartSeries)
