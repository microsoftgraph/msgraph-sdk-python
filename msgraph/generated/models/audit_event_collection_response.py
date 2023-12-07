from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .audit_event import AuditEvent
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AuditEventCollectionResponse(BaseCollectionPaginationCountResponse[AuditEvent]):
    value: Optional[List[AuditEvent]] = None

    def __init__(self):
        super().__init__(entity=AuditEvent)
