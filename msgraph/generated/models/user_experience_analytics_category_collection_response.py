from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_category import UserExperienceAnalyticsCategory


@dataclass
class UserExperienceAnalyticsCategoryCollectionResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsCategory]
):
    value: Optional[List[UserExperienceAnalyticsCategory]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsCategory)
