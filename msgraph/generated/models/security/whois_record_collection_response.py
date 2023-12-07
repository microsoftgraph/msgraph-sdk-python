from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .whois_record import WhoisRecord


@dataclass
class WhoisRecordCollectionResponse(BaseCollectionPaginationCountResponse[WhoisRecord]):
    value: Optional[List[WhoisRecord]] = None

    def __init__(self):
        super().__init__(entity=WhoisRecord)
