from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .android_managed_app_protection import AndroidManagedAppProtection
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AndroidManagedAppProtectionCollectionResponse(
    BaseCollectionPaginationCountResponse[AndroidManagedAppProtection]
):
    value: Optional[List[AndroidManagedAppProtection]] = None

    def __init__(self):
        super().__init__(entity=AndroidManagedAppProtection)
