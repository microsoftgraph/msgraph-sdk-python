from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_operation import WorkbookOperation


@dataclass
class WorkbookOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookOperation]
):
    value: Optional[List[WorkbookOperation]] = None

    def __init__(self):
        super().__init__(entity=WorkbookOperation)
