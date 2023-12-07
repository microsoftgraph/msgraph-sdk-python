from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .secure_score import SecureScore


@dataclass
class SecureScoreCollectionResponse(BaseCollectionPaginationCountResponse[SecureScore]):
    value: Optional[List[SecureScore]] = None

    def __init__(self):
        super().__init__(entity=SecureScore)
