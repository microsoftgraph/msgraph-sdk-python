from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance


@dataclass
class UserExperienceAnalyticsDevicePerformanceCollectionResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsDevicePerformance]
):
    value: Optional[List[UserExperienceAnalyticsDevicePerformance]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsDevicePerformance)
