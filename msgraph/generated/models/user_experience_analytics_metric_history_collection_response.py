from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory


@dataclass
class UserExperienceAnalyticsMetricHistoryCollectionResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsMetricHistory]
):
    value: Optional[List[UserExperienceAnalyticsMetricHistory]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsMetricHistory)
