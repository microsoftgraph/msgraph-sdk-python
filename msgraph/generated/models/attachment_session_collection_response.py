from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .attachment_session import AttachmentSession
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AttachmentSessionCollectionResponse(
    BaseCollectionPaginationCountResponse[AttachmentSession]
):
    value: Optional[List[AttachmentSession]] = None

    def __init__(self):
        super().__init__(entity=AttachmentSession)
