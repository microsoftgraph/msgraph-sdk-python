from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .attachment_base import AttachmentBase
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AttachmentBaseCollectionResponse(
    BaseCollectionPaginationCountResponse[AttachmentBase]
):
    value: Optional[List[AttachmentBase]] = None

    def __init__(self):
        super().__init__(entity=AttachmentBase)
