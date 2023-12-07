from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.user_experience_analytics_device_performance import (
    UserExperienceAnalyticsDevicePerformance,
)


@dataclass
class SummarizeDevicePerformanceDevicesWithSummarizeByGetResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsDevicePerformance]
):
    value: Optional[List[UserExperienceAnalyticsDevicePerformance]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsDevicePerformance)
