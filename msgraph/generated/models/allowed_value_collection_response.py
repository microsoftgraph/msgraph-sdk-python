from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .allowed_value import AllowedValue
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AllowedValueCollectionResponse(
    BaseCollectionPaginationCountResponse[AllowedValue]
):
    value: Optional[List[AllowedValue]] = None

    def __init__(self):
        super().__init__(entity=AllowedValue)
