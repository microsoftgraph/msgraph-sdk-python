from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .end_user_notification_detail import EndUserNotificationDetail


@dataclass
class EndUserNotificationDetailCollectionResponse(
    BaseCollectionPaginationCountResponse[EndUserNotificationDetail]
):
    value: Optional[List[EndUserNotificationDetail]] = None

    def __init__(self):
        super().__init__(entity=EndUserNotificationDetail)
