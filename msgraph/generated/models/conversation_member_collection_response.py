from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .conversation_member import ConversationMember


@dataclass
class ConversationMemberCollectionResponse(
    BaseCollectionPaginationCountResponse[ConversationMember]
):
    value: Optional[List[ConversationMember]] = None

    def __init__(self):
        super().__init__(entity=ConversationMember)
