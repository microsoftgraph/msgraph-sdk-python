from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory


@dataclass
class UserExperienceAnalyticsScoreHistoryCollectionResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsScoreHistory]
):
    value: Optional[List[UserExperienceAnalyticsScoreHistory]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsScoreHistory)
