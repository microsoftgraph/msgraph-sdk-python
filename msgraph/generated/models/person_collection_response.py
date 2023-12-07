from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .person import Person


@dataclass
class PersonCollectionResponse(BaseCollectionPaginationCountResponse[Person]):
    value: Optional[List[Person]] = None

    def __init__(self):
        super().__init__(entity=Person)
