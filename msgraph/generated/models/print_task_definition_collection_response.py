from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .print_task_definition import PrintTaskDefinition


@dataclass
class PrintTaskDefinitionCollectionResponse(
    BaseCollectionPaginationCountResponse[PrintTaskDefinition]
):
    value: Optional[List[PrintTaskDefinition]] = None

    def __init__(self):
        super().__init__(entity=PrintTaskDefinition)
