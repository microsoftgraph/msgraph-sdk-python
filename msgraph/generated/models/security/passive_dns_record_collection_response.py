from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .passive_dns_record import PassiveDnsRecord


@dataclass
class PassiveDnsRecordCollectionResponse(
    BaseCollectionPaginationCountResponse[PassiveDnsRecord]
):
    value: Optional[List[PassiveDnsRecord]] = None

    def __init__(self):
        super().__init__(entity=PassiveDnsRecord)
