from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .article import Article


@dataclass
class ArticleCollectionResponse(BaseCollectionPaginationCountResponse[Article]):
    value: Optional[List[Article]] = None

    def __init__(self):
        super().__init__(entity=Article)
