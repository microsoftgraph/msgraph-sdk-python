from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .message import Message


@dataclass
class MessageCollectionResponse(BaseCollectionPaginationCountResponse[Message]):
    value: Optional[List[Message]] = None

    def __init__(self):
        super().__init__(entity=Message)
