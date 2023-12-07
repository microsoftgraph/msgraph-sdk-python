from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workflow import Workflow


@dataclass
class WorkflowCollectionResponse(BaseCollectionPaginationCountResponse[Workflow]):
    value: Optional[List[Workflow]] = None

    def __init__(self):
        super().__init__(entity=Workflow)
