from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .directory_audit import DirectoryAudit


@dataclass
class DirectoryAuditCollectionResponse(
    BaseCollectionPaginationCountResponse[DirectoryAudit]
):
    value: Optional[List[DirectoryAudit]] = None

    def __init__(self):
        super().__init__(entity=DirectoryAudit)
