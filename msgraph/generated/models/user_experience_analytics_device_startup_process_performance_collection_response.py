from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_device_startup_process_performance import (
    UserExperienceAnalyticsDeviceStartupProcessPerformance,
)


@dataclass
class UserExperienceAnalyticsDeviceStartupProcessPerformanceCollectionResponse(
    BaseCollectionPaginationCountResponse[
        UserExperienceAnalyticsDeviceStartupProcessPerformance
    ]
):
    value: Optional[List[UserExperienceAnalyticsDeviceStartupProcessPerformance]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsDeviceStartupProcessPerformance)
