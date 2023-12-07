from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .external_activity import ExternalActivity


@dataclass
class ExternalActivityCollectionResponse(
    BaseCollectionPaginationCountResponse[ExternalActivity]
):
    value: Optional[List[ExternalActivity]] = None

    def __init__(self):
        super().__init__(entity=ExternalActivity)
