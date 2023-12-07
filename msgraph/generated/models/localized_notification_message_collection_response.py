from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .localized_notification_message import LocalizedNotificationMessage


@dataclass
class LocalizedNotificationMessageCollectionResponse(
    BaseCollectionPaginationCountResponse[LocalizedNotificationMessage]
):
    value: Optional[List[LocalizedNotificationMessage]] = None

    def __init__(self):
        super().__init__(entity=LocalizedNotificationMessage)
