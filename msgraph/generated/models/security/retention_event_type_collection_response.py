from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .retention_event_type import RetentionEventType


@dataclass
class RetentionEventTypeCollectionResponse(
    BaseCollectionPaginationCountResponse[RetentionEventType]
):
    value: Optional[List[RetentionEventType]] = None

    def __init__(self):
        super().__init__(entity=RetentionEventType)
