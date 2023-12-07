from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_processing_result import UserProcessingResult


@dataclass
class UserProcessingResultCollectionResponse(
    BaseCollectionPaginationCountResponse[UserProcessingResult]
):
    value: Optional[List[UserProcessingResult]] = None

    def __init__(self):
        super().__init__(entity=UserProcessingResult)
