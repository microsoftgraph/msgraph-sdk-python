from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .print_task_trigger import PrintTaskTrigger


@dataclass
class PrintTaskTriggerCollectionResponse(
    BaseCollectionPaginationCountResponse[PrintTaskTrigger]
):
    value: Optional[List[PrintTaskTrigger]] = None

    def __init__(self):
        super().__init__(entity=PrintTaskTrigger)
