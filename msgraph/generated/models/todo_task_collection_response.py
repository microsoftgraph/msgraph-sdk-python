from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .todo_task import TodoTask


@dataclass
class TodoTaskCollectionResponse(BaseCollectionPaginationCountResponse[TodoTask]):
    value: Optional[List[TodoTask]] = None

    def __init__(self):
        super().__init__(entity=TodoTask)
