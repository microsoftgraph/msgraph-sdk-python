from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_experience_analytics_device_startup_process import (
    UserExperienceAnalyticsDeviceStartupProcess,
)


@dataclass
class UserExperienceAnalyticsDeviceStartupProcessCollectionResponse(
    BaseCollectionPaginationCountResponse[UserExperienceAnalyticsDeviceStartupProcess]
):
    value: Optional[List[UserExperienceAnalyticsDeviceStartupProcess]] = None

    def __init__(self):
        super().__init__(entity=UserExperienceAnalyticsDeviceStartupProcess)
