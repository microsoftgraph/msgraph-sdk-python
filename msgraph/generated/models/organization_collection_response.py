from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .organization import Organization


@dataclass
class OrganizationCollectionResponse(
    BaseCollectionPaginationCountResponse[Organization]
):
    value: Optional[List[Organization]] = None

    def __init__(self):
        super().__init__(entity=Organization)
