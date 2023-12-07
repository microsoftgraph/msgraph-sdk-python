from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .whois_history_record import WhoisHistoryRecord


@dataclass
class WhoisHistoryRecordCollectionResponse(
    BaseCollectionPaginationCountResponse[WhoisHistoryRecord]
):
    value: Optional[List[WhoisHistoryRecord]] = None

    def __init__(self):
        super().__init__(entity=WhoisHistoryRecord)
