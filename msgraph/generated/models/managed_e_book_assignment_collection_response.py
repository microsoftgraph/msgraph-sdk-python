from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_e_book_assignment import ManagedEBookAssignment


@dataclass
class ManagedEBookAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[ManagedEBookAssignment]
):
    value: Optional[List[ManagedEBookAssignment]] = None

    def __init__(self):
        super().__init__(entity=ManagedEBookAssignment)
