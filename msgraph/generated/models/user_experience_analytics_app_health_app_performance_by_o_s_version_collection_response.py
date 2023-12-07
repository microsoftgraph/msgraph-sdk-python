from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_app_health_app_performance_by_o_s_version import (
    UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion,
)


@dataclass
class UserExperienceAnalyticsAppHealthAppPerformanceByOSVersionCollectionResponse(
    BaseCollectionPaginationCountResponse[
        UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
    ]
):
    value: Optional[
        List[UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion]
    ] = None

    def __init__(self):
        super().__init__(
            entity=UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
        )
