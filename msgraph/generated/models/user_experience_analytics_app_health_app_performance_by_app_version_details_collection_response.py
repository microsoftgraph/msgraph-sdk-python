from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_app_health_app_performance_by_app_version_details import (
    UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails,
)


@dataclass
class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetailsCollectionResponse(
    BaseCollectionPaginationCountResponse[
        UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
    ]
):
    value: Optional[
        List[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails]
    ] = None

    def __init__(self):
        super().__init__(
            entity=UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
        )
