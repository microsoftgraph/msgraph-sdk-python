from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_app_health_device_model_performance import (
    UserExperienceAnalyticsAppHealthDeviceModelPerformance,
)


@dataclass
class UserExperienceAnalyticsAppHealthDeviceModelPerformanceCollectionResponse(
    BaseCollectionPaginationCountResponse[
        UserExperienceAnalyticsAppHealthDeviceModelPerformance
    ]
):
    value: Optional[List[UserExperienceAnalyticsAppHealthDeviceModelPerformance]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsAppHealthDeviceModelPerformance)
