from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .alert import Alert
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AlertCollectionResponse(BaseCollectionPaginationCountResponse[Alert]):
    value: Optional[List[Alert]] = None

    def __init__(self):
        super().__init__(entity=Alert)
