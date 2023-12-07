from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .approval_stage import ApprovalStage
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class ApprovalStageCollectionResponse(
    BaseCollectionPaginationCountResponse[ApprovalStage]
):
    value: Optional[List[ApprovalStage]] = None

    def __init__(self):
        super().__init__(entity=ApprovalStage)
