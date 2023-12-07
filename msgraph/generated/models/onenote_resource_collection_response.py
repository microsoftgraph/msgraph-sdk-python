from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .onenote_resource import OnenoteResource


@dataclass
class OnenoteResourceCollectionResponse(
    BaseCollectionPaginationCountResponse[OnenoteResource]
):
    value: Optional[List[OnenoteResource]] = None

    def __init__(self):
        super().__init__(entity=OnenoteResource)
