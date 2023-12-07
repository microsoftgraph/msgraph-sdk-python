from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .external_item import ExternalItem


@dataclass
class ExternalItemCollectionResponse(
    BaseCollectionPaginationCountResponse[ExternalItem]
):
    value: Optional[List[ExternalItem]] = None

    def __init__(self):
        super().__init__(entity=ExternalItem)
