from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .named_location import NamedLocation


@dataclass
class NamedLocationCollectionResponse(
    BaseCollectionPaginationCountResponse[NamedLocation]
):
    value: Optional[List[NamedLocation]] = None

    def __init__(self):
        super().__init__(entity=NamedLocation)
