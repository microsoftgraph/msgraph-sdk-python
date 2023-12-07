from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .shift import Shift


@dataclass
class ShiftCollectionResponse(BaseCollectionPaginationCountResponse[Shift]):
    value: Optional[List[Shift]] = None

    def __init__(self):
        super().__init__(entity=Shift)
