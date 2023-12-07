from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .contact import Contact


@dataclass
class ContactCollectionResponse(BaseCollectionPaginationCountResponse[Contact]):
    value: Optional[List[Contact]] = None

    def __init__(self):
        super().__init__(entity=Contact)
