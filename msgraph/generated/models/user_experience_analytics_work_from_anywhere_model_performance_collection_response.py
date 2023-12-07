from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_work_from_anywhere_model_performance import (
    UserExperienceAnalyticsWorkFromAnywhereModelPerformance,
)


@dataclass
class UserExperienceAnalyticsWorkFromAnywhereModelPerformanceCollectionResponse(
    BaseCollectionPaginationCountResponse[
        UserExperienceAnalyticsWorkFromAnywhereModelPerformance
    ]
):
    value: Optional[
        List[UserExperienceAnalyticsWorkFromAnywhereModelPerformance]
    ] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsWorkFromAnywhereModelPerformance)
