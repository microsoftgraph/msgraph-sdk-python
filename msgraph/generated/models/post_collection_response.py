from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .post import Post


@dataclass
class PostCollectionResponse(BaseCollectionPaginationCountResponse[Post]):
    value: Optional[List[Post]] = None

    def __init__(self):
        super().__init__(entity=Post)
