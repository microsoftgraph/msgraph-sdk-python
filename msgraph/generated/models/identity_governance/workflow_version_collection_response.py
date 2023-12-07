from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workflow_version import WorkflowVersion


@dataclass
class WorkflowVersionCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkflowVersion]
):
    value: Optional[List[WorkflowVersion]] = None

    def __init__(self):
        super().__init__(entity=WorkflowVersion)
