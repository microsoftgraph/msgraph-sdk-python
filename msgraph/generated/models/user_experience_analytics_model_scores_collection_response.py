from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores


@dataclass
class UserExperienceAnalyticsModelScoresCollectionResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsModelScores]
):
    value: Optional[List[UserExperienceAnalyticsModelScores]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsModelScores)
