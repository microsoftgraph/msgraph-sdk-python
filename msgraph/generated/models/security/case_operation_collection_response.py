from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .case_operation import CaseOperation


@dataclass
class CaseOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[CaseOperation]
):
    value: Optional[List[CaseOperation]] = None

    def __init__(self):
        super().__init__(entity=CaseOperation)
