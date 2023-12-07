from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .conversation_thread import ConversationThread


@dataclass
class ConversationThreadCollectionResponse(
    BaseCollectionPaginationCountResponse[ConversationThread]
):
    value: Optional[List[ConversationThread]] = None

    def __init__(self):
        super().__init__(entity=ConversationThread)
