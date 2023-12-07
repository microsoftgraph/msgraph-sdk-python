from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .vpp_token import VppToken


@dataclass
class VppTokenCollectionResponse(BaseCollectionPaginationCountResponse[VppToken]):
    value: Optional[List[VppToken]] = None

    def __init__(self):
        super().__init__(entity=VppToken)
