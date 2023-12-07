from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .extension import Extension


@dataclass
class ExtensionCollectionResponse(BaseCollectionPaginationCountResponse[Extension]):
    value: Optional[List[Extension]] = None

    def __init__(self):
        super().__init__(entity=Extension)
