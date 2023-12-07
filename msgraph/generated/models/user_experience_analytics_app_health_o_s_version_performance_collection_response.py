from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_app_health_o_s_version_performance import (
    UserExperienceAnalyticsAppHealthOSVersionPerformance,
)


@dataclass
class UserExperienceAnalyticsAppHealthOSVersionPerformanceCollectionResponse(
    BaseCollectionPaginationCountResponse[
        UserExperienceAnalyticsAppHealthOSVersionPerformance
    ]
):
    value: Optional[List[UserExperienceAnalyticsAppHealthOSVersionPerformance]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsAppHealthOSVersionPerformance)
