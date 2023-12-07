from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_work_from_anywhere_metric import (
    UserExperienceAnalyticsWorkFromAnywhereMetric,
)


@dataclass
class UserExperienceAnalyticsWorkFromAnywhereMetricCollectionResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsWorkFromAnywhereMetric]
):
    value: Optional[List[UserExperienceAnalyticsWorkFromAnywhereMetric]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsWorkFromAnywhereMetric)
