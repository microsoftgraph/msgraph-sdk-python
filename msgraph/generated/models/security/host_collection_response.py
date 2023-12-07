from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .host import Host


@dataclass
class HostCollectionResponse(BaseCollectionPaginationCountResponse[Host]):
    value: Optional[List[Host]] = None

    def __init__(self):
        super().__init__(entity=Host)
