from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import (
    UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId,
)


@dataclass
class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceIdCollectionResponse(
    BaseCollectionPaginationCountResponse[
        UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
    ]
):
    value: Optional[
        List[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId]
    ] = None

    def __init__(self):
        super().__init__(
            entity=UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
        )
