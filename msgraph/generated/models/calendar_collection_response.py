from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .calendar import Calendar


@dataclass
class CalendarCollectionResponse(BaseCollectionPaginationCountResponse[Calendar]):
    value: Optional[List[Calendar]] = None

    def __init__(self):
        super().__init__(entity=Calendar)
