from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .task_processing_result import TaskProcessingResult


@dataclass
class TaskProcessingResultCollectionResponse(
    BaseCollectionPaginationCountResponse[TaskProcessingResult]
):
    value: Optional[List[TaskProcessingResult]] = None

    def __init__(self):
        super().__init__(entity=TaskProcessingResult)
