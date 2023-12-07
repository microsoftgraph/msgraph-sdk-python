from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .chat_message import ChatMessage


@dataclass
class ChatMessageCollectionResponse(BaseCollectionPaginationCountResponse[ChatMessage]):
    value: Optional[List[ChatMessage]] = None

    def __init__(self):
        super().__init__(entity=ChatMessage)
