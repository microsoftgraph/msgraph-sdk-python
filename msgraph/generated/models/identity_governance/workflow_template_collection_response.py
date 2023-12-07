from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .workflow_template import WorkflowTemplate


@dataclass
class WorkflowTemplateCollectionResponse(
    BaseCollectionPaginationCountResponse[WorkflowTemplate]
):
    value: Optional[List[WorkflowTemplate]] = None

    def __init__(self):
        super().__init__(entity=WorkflowTemplate)
