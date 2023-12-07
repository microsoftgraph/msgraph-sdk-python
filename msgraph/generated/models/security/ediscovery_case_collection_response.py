from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ediscovery_case import EdiscoveryCase


@dataclass
class EdiscoveryCaseCollectionResponse(
    BaseCollectionPaginationCountResponse[EdiscoveryCase]
):
    value: Optional[List[EdiscoveryCase]] = None

    def __init__(self):
        super().__init__(entity=EdiscoveryCase)
