from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .synchronization_template import SynchronizationTemplate


@dataclass
class SynchronizationTemplateCollectionResponse(
    BaseCollectionPaginationCountResponse[SynchronizationTemplate]
):
    value: Optional[List[SynchronizationTemplate]] = None

    def __init__(self):
        super().__init__(entity=SynchronizationTemplate)
