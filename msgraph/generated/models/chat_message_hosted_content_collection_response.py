from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .chat_message_hosted_content import ChatMessageHostedContent


@dataclass
class ChatMessageHostedContentCollectionResponse(
    BaseCollectionPaginationCountResponse[ChatMessageHostedContent]
):
    value: Optional[List[ChatMessageHostedContent]] = None

    def __init__(self):
        super().__init__(entity=ChatMessageHostedContent)
