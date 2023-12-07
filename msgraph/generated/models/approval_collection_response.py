from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .approval import Approval
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class ApprovalCollectionResponse(BaseCollectionPaginationCountResponse[Approval]):
    value: Optional[List[Approval]] = None

    def __init__(self):
        super().__init__(entity=Approval)
