from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .contract import Contract


@dataclass
class ContractCollectionResponse(BaseCollectionPaginationCountResponse[Contract]):
    value: Optional[List[Contract]] = None

    def __init__(self):
        super().__init__(entity=Contract)
