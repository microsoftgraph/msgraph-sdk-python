from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .task_definition import TaskDefinition


@dataclass
class TaskDefinitionCollectionResponse(
    BaseCollectionPaginationCountResponse[TaskDefinition]
):
    value: Optional[List[TaskDefinition]] = None

    def __init__(self):
        super().__init__(entity=TaskDefinition)
