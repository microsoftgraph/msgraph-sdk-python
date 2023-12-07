from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .risky_user import RiskyUser


@dataclass
class RiskyUserCollectionResponse(BaseCollectionPaginationCountResponse[RiskyUser]):
    value: Optional[List[RiskyUser]] = None

    def __init__(self):
        super().__init__(entity=RiskyUser)
