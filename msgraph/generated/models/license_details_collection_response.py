from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .license_details import LicenseDetails


@dataclass
class LicenseDetailsCollectionResponse(
    BaseCollectionPaginationCountResponse[LicenseDetails]
):
    value: Optional[List[LicenseDetails]] = None

    def __init__(self):
        super().__init__(entity=LicenseDetails)
