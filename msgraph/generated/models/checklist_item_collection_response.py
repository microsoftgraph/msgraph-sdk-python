from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .checklist_item import ChecklistItem


@dataclass
class ChecklistItemCollectionResponse(
    BaseCollectionPaginationCountResponse[ChecklistItem]
):
    value: Optional[List[ChecklistItem]] = None

    def __init__(self):
        super().__init__(entity=ChecklistItem)
