from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_table_row import WorkbookTableRow


@dataclass
class WorkbookTableRowCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookTableRow]
):
    value: Optional[List[WorkbookTableRow]] = None

    def __init__(self):
        super().__init__(entity=WorkbookTableRow)
