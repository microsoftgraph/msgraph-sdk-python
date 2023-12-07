from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .learning_provider import LearningProvider


@dataclass
class LearningProviderCollectionResponse(
    BaseCollectionPaginationCountResponse[LearningProvider]
):
    value: Optional[List[LearningProvider]] = None

    def __init__(self):
        super().__init__(entity=LearningProvider)
