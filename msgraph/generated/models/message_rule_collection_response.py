from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .message_rule import MessageRule


@dataclass
class MessageRuleCollectionResponse(BaseCollectionPaginationCountResponse[MessageRule]):
    value: Optional[List[MessageRule]] = None

    def __init__(self):
        super().__init__(entity=MessageRule)
