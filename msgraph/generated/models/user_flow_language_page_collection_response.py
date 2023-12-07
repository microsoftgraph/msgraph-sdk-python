from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_flow_language_page import UserFlowLanguagePage


@dataclass
class UserFlowLanguagePageCollectionResponse(
    BaseCollectionPaginationCountResponse[UserFlowLanguagePage]
):
    value: Optional[List[UserFlowLanguagePage]] = None

    def __init__(self):
        super().__init__(entity=UserFlowLanguagePage)
