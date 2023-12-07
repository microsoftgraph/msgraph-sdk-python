from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .content_sharing_session import ContentSharingSession


@dataclass
class ContentSharingSessionCollectionResponse(
    BaseCollectionPaginationCountResponse[ContentSharingSession]
):
    value: Optional[List[ContentSharingSession]] = None

    def __init__(self):
        super().__init__(entity=ContentSharingSession)
