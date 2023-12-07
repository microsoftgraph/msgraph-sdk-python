from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_app_health_device_performance_details import (
    UserExperienceAnalyticsAppHealthDevicePerformanceDetails,
)


@dataclass
class UserExperienceAnalyticsAppHealthDevicePerformanceDetailsCollectionResponse(
    BaseCollectionPaginationCountResponse[
        UserExperienceAnalyticsAppHealthDevicePerformanceDetails
    ]
):
    value: Optional[
        List[UserExperienceAnalyticsAppHealthDevicePerformanceDetails]
    ] = None

    def __init__(self):
        super().__init__(
            entity=UserExperienceAnalyticsAppHealthDevicePerformanceDetails
        )
