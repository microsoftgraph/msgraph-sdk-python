from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .todo_task_list import TodoTaskList


@dataclass
class TodoTaskListCollectionResponse(
    BaseCollectionPaginationCountResponse[TodoTaskList]
):
    value: Optional[List[TodoTaskList]] = None

    def __init__(self):
        super().__init__(entity=TodoTaskList)
