from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .pinned_chat_message_info import PinnedChatMessageInfo


@dataclass
class PinnedChatMessageInfoCollectionResponse(
    BaseCollectionPaginationCountResponse[PinnedChatMessageInfo]
):
    value: Optional[List[PinnedChatMessageInfo]] = None

    def __init__(self):
        super().__init__(entity=PinnedChatMessageInfo)
