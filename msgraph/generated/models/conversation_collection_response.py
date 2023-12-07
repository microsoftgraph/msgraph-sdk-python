from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .conversation import Conversation


@dataclass
class ConversationCollectionResponse(
    BaseCollectionPaginationCountResponse[Conversation]
):
    value: Optional[List[Conversation]] = None

    def __init__(self):
        super().__init__(entity=Conversation)
