from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_mobile_app import ManagedMobileApp


@dataclass
class ManagedMobileAppCollectionResponse(
    BaseCollectionPaginationCountResponse[ManagedMobileApp]
):
    value: Optional[List[ManagedMobileApp]] = None

    def __init__(self):
        super().__init__(entity=ManagedMobileApp)
