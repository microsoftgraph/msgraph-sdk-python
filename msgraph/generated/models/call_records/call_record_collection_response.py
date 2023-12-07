from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .call_record import CallRecord


@dataclass
class CallRecordCollectionResponse(BaseCollectionPaginationCountResponse[CallRecord]):
    value: Optional[List[CallRecord]] = None

    def __init__(self):
        super().__init__(entity=CallRecord)
