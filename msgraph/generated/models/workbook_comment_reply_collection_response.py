from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workbook_comment_reply import WorkbookCommentReply


@dataclass
class WorkbookCommentReplyCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkbookCommentReply]
):
    value: Optional[List[WorkbookCommentReply]] = None

    def __init__(self):
        super().__init__(entity=WorkbookCommentReply)
