from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .document_set_version import DocumentSetVersion


@dataclass
class DocumentSetVersionCollectionResponse(
    BaseCollectionPaginationCountResponse[DocumentSetVersion]
):
    value: Optional[List[DocumentSetVersion]] = None

    def __init__(self):
        super().__init__(entity=DocumentSetVersion)
