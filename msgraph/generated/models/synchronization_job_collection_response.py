from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .synchronization_job import SynchronizationJob


@dataclass
class SynchronizationJobCollectionResponse(
    BaseCollectionPaginationCountResponse[SynchronizationJob]
):
    value: Optional[List[SynchronizationJob]] = None

    def __init__(self):
        super().__init__(entity=SynchronizationJob)
