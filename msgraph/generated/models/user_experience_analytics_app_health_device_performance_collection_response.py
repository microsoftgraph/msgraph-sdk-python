from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_app_health_device_performance import (
    UserExperienceAnalyticsAppHealthDevicePerformance,
)


@dataclass
class UserExperienceAnalyticsAppHealthDevicePerformanceCollectionResponse(
    BaseCollectionPaginationCountResponse[
        UserExperienceAnalyticsAppHealthDevicePerformance
    ]
):
    value: Optional[List[UserExperienceAnalyticsAppHealthDevicePerformance]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsAppHealthDevicePerformance)
