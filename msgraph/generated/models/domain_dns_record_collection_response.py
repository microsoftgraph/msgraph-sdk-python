from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .domain_dns_record import DomainDnsRecord


@dataclass
class DomainDnsRecordCollectionResponse(
    BaseCollectionPaginationCountResponse[DomainDnsRecord]
):
    value: Optional[List[DomainDnsRecord]] = None

    def __init__(self):
        super().__init__(entity=DomainDnsRecord)
