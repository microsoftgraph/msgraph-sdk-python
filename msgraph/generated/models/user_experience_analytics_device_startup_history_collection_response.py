from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_device_startup_history import (
    UserExperienceAnalyticsDeviceStartupHistory,
)


@dataclass
class UserExperienceAnalyticsDeviceStartupHistoryCollectionResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsDeviceStartupHistory]
):
    value: Optional[List[UserExperienceAnalyticsDeviceStartupHistory]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsDeviceStartupHistory)
