from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .end_user_notification import EndUserNotification


@dataclass
class EndUserNotificationCollectionResponse(
    BaseCollectionPaginationCountResponse[EndUserNotification]
):
    value: Optional[List[EndUserNotification]] = None

    def __init__(self):
        super().__init__(entity=EndUserNotification)
