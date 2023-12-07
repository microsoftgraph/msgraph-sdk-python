from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .chat import Chat


@dataclass
class ChatCollectionResponse(BaseCollectionPaginationCountResponse[Chat]):
    value: Optional[List[Chat]] = None

    def __init__(self):
        super().__init__(entity=Chat)
