from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_comment import WorkbookComment


@dataclass
class WorkbookCommentCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookComment]
):
    value: Optional[List[WorkbookComment]] = None

    def __init__(self):
        super().__init__(entity=WorkbookComment)
