from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .host_component import HostComponent


@dataclass
class HostComponentCollectionResponse(
    BaseCollectionPaginationCountResponse[HostComponent]
):
    value: Optional[List[HostComponent]] = None

    def __init__(self):
        super().__init__(entity=HostComponent)
