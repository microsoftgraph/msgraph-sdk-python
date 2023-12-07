from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .external_connection import ExternalConnection


@dataclass
class ExternalConnectionCollectionResponse(
    BaseCollectionPaginationCountResponse[ExternalConnection]
):
    value: Optional[List[ExternalConnection]] = None

    def __init__(self):
        super().__init__(entity=ExternalConnection)
