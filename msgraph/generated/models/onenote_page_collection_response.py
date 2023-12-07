from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .onenote_page import OnenotePage


@dataclass
class OnenotePageCollectionResponse(BaseCollectionPaginationCountResponse[OnenotePage]):
    value: Optional[List[OnenotePage]] = None

    def __init__(self):
        super().__init__(entity=OnenotePage)
