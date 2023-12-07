from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .external_group import ExternalGroup


@dataclass
class ExternalGroupCollectionResponse(
    BaseCollectionPaginationCountResponse[ExternalGroup]
):
    value: Optional[List[ExternalGroup]] = None

    def __init__(self):
        super().__init__(entity=ExternalGroup)
