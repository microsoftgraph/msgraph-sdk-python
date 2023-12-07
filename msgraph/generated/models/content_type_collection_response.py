from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .content_type import ContentType


@dataclass
class ContentTypeCollectionResponse(BaseCollectionPaginationCountResponse[ContentType]):
    value: Optional[List[ContentType]] = None

    def __init__(self):
        super().__init__(entity=ContentType)
