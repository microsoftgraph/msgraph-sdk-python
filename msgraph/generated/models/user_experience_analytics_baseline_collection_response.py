from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline


@dataclass
class UserExperienceAnalyticsBaselineCollectionResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsBaseline]
):
    value: Optional[List[UserExperienceAnalyticsBaseline]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsBaseline)
