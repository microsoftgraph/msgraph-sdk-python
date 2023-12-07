from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .linked_resource import LinkedResource


@dataclass
class LinkedResourceCollectionResponse(
    BaseCollectionPaginationCountResponse[LinkedResource]
):
    value: Optional[List[LinkedResource]] = None

    def __init__(self):
        super().__init__(entity=LinkedResource)
