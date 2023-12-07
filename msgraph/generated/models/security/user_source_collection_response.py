from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_source import UserSource


@dataclass
class UserSourceCollectionResponse(BaseCollectionPaginationCountResponse[UserSource]):
    value: Optional[List[UserSource]] = None

    def __init__(self):
        super().__init__(entity=UserSource)
