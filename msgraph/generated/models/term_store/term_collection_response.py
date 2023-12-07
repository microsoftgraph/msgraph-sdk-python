from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .term import Term


@dataclass
class TermCollectionResponse(BaseCollectionPaginationCountResponse[Term]):
    value: Optional[List[Term]] = None

    def __init__(self):
        super().__init__(entity=Term)
