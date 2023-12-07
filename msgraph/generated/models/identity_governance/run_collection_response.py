from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .run import Run


@dataclass
class RunCollectionResponse(BaseCollectionPaginationCountResponse[Run]):
    value: Optional[List[Run]] = None

    def __init__(self):
        super().__init__(entity=Run)
