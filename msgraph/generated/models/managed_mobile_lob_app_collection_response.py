from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_mobile_lob_app import ManagedMobileLobApp


@dataclass
class ManagedMobileLobAppCollectionResponse(
    BaseCollectionPaginationCountResponse[ManagedMobileLobApp]
):
    value: Optional[List[ManagedMobileLobApp]] = None

    def __init__(self):
        super().__init__(entity=ManagedMobileLobApp)
