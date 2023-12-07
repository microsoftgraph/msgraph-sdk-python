from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_metric import UserExperienceAnalyticsMetric


@dataclass
class UserExperienceAnalyticsMetricCollectionResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsMetric]
):
    value: Optional[List[UserExperienceAnalyticsMetric]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsMetric)
