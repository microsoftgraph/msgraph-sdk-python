from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .article_indicator import ArticleIndicator


@dataclass
class ArticleIndicatorCollectionResponse(
    BaseCollectionPaginationCountResponse[ArticleIndicator]
):
    value: Optional[List[ArticleIndicator]] = None

    def __init__(self):
        super().__init__(entity=ArticleIndicator)
