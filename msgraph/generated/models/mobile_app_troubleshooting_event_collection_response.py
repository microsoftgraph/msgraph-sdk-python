from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent


@dataclass
class MobileAppTroubleshootingEventCollectionResponse(
    BaseCollectionPaginationCountResponse[MobileAppTroubleshootingEvent]
):
    value: Optional[List[MobileAppTroubleshootingEvent]] = None

    def __init__(self):
        super().__init__(entity=MobileAppTroubleshootingEvent)
