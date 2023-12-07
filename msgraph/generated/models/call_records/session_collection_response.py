from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .session import Session


@dataclass
class SessionCollectionResponse(BaseCollectionPaginationCountResponse[Session]):
    value: Optional[List[Session]] = None

    def __init__(self):
        super().__init__(entity=Session)
