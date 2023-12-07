from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .section_group import SectionGroup


@dataclass
class SectionGroupCollectionResponse(
    BaseCollectionPaginationCountResponse[SectionGroup]
):
    value: Optional[List[SectionGroup]] = None

    def __init__(self):
        super().__init__(entity=SectionGroup)
