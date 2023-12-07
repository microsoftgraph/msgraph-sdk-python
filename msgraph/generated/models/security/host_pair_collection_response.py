from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .host_pair import HostPair


@dataclass
class HostPairCollectionResponse(BaseCollectionPaginationCountResponse[HostPair]):
    value: Optional[List[HostPair]] = None

    def __init__(self):
        super().__init__(entity=HostPair)
