from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .identity import Identity


@dataclass
class IdentityCollectionResponse(BaseCollectionPaginationCountResponse[Identity]):
    value: Optional[List[Identity]] = None

    def __init__(self):
        super().__init__(entity=Identity)
