from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .service_announcement_attachment import ServiceAnnouncementAttachment


@dataclass
class ServiceAnnouncementAttachmentCollectionResponse(
    BaseCollectionPaginationCountResponse[ServiceAnnouncementAttachment]
):
    value: Optional[List[ServiceAnnouncementAttachment]] = None

    def __init__(self):
        super().__init__(entity=ServiceAnnouncementAttachment)
