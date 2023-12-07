from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .learning_content import LearningContent


@dataclass
class LearningContentCollectionResponse(
    BaseCollectionPaginationCountResponse[LearningContent]
):
    value: Optional[List[LearningContent]] = None

    def __init__(self):
        super().__init__(entity=LearningContent)
