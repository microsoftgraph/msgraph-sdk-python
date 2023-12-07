from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_worksheet import WorkbookWorksheet


@dataclass
class WorkbookWorksheetCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookWorksheet]
):
    value: Optional[List[WorkbookWorksheet]] = None

    def __init__(self):
        super().__init__(entity=WorkbookWorksheet)
