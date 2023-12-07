from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_app_health_application_performance import (
    UserExperienceAnalyticsAppHealthApplicationPerformance,
)


@dataclass
class UserExperienceAnalyticsAppHealthApplicationPerformanceCollectionResponse(
    BaseCollectionPaginationCountResponse[
        UserExperienceAnalyticsAppHealthApplicationPerformance
    ]
):
    value: Optional[List[UserExperienceAnalyticsAppHealthApplicationPerformance]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsAppHealthApplicationPerformance)
