from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .onenote_section import OnenoteSection


@dataclass
class OnenoteSectionCollectionResponse(
    BaseCollectionPaginationCountResponse[OnenoteSection]
):
    value: Optional[List[OnenoteSection]] = None

    def __init__(self):
        super().__init__(entity=OnenoteSection)
