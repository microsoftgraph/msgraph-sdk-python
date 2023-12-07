from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .attachment import Attachment
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AttachmentCollectionResponse(BaseCollectionPaginationCountResponse[Attachment]):
    value: Optional[List[Attachment]] = None

    def __init__(self):
        super().__init__(entity=Attachment)
