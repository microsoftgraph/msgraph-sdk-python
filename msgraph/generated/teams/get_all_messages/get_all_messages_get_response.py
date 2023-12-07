from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ...models.chat_message import ChatMessage


@dataclass
class GetAllMessagesGetResponse(BaseCollectionPaginationCountResponse[ChatMessage]):
    value: Optional[List[ChatMessage]] = None

    def __init__(self):
        super().__init__(entity=ChatMessage)
