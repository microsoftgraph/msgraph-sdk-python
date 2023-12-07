from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores


@dataclass
class UserExperienceAnalyticsDeviceScoresCollectionResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsDeviceScores]
):
    value: Optional[List[UserExperienceAnalyticsDeviceScores]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsDeviceScores)
