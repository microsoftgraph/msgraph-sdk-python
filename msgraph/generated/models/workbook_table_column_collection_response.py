from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_table_column import WorkbookTableColumn


@dataclass
class WorkbookTableColumnCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookTableColumn]
):
    value: Optional[List[WorkbookTableColumn]] = None

    def __init__(self):
        super().__init__(entity=WorkbookTableColumn)
