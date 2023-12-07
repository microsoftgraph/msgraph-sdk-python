from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mobile_contained_app import MobileContainedApp


@dataclass
class MobileContainedAppCollectionResponse(
    BaseCollectionPaginationCountResponse[MobileContainedApp]
):
    value: Optional[List[MobileContainedApp]] = None

    def __init__(self):
        super().__init__(entity=MobileContainedApp)
