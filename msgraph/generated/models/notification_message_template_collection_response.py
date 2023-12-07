from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .notification_message_template import NotificationMessageTemplate


@dataclass
class NotificationMessageTemplateCollectionResponse(
    BaseCollectionPaginationCountResponse[NotificationMessageTemplate]
):
    value: Optional[List[NotificationMessageTemplate]] = None

    def __init__(self):
        super().__init__(entity=NotificationMessageTemplate)
