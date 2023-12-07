from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ios_managed_app_protection import IosManagedAppProtection


@dataclass
class IosManagedAppProtectionCollectionResponse(
    BaseCollectionPaginationCountResponse[IosManagedAppProtection]
):
    value: Optional[List[IosManagedAppProtection]] = None

    def __init__(self):
        super().__init__(entity=IosManagedAppProtection)
