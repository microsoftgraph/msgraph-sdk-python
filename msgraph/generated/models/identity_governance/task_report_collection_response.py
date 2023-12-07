from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .task_report import TaskReport


@dataclass
class TaskReportCollectionResponse(BaseCollectionPaginationCountResponse[TaskReport]):
    value: Optional[List[TaskReport]] = None

    def __init__(self):
        super().__init__(entity=TaskReport)
