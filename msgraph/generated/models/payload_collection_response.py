from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .payload import Payload


@dataclass
class PayloadCollectionResponse(BaseCollectionPaginationCountResponse[Payload]):
    value: Optional[List[Payload]] = None

    def __init__(self):
        super().__init__(entity=Payload)
