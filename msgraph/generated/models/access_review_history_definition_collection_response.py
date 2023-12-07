from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_review_history_definition import AccessReviewHistoryDefinition
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessReviewHistoryDefinitionCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessReviewHistoryDefinition]
):
    value: Optional[List[AccessReviewHistoryDefinition]] = None

    def __init__(self):
        super().__init__(entity=AccessReviewHistoryDefinition)
