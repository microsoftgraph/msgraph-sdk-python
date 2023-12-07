from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .training_language_detail import TrainingLanguageDetail


@dataclass
class TrainingLanguageDetailCollectionResponse(
    BaseCollectionPaginationCountResponse[TrainingLanguageDetail]
):
    value: Optional[List[TrainingLanguageDetail]] = None

    def __init__(self):
        super().__init__(entity=TrainingLanguageDetail)
