from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .default_managed_app_protection import DefaultManagedAppProtection


@dataclass
class DefaultManagedAppProtectionCollectionResponse(
    BaseCollectionPaginationCountResponse[DefaultManagedAppProtection]
):
    value: Optional[List[DefaultManagedAppProtection]] = None

    def __init__(self):
        super().__init__(entity=DefaultManagedAppProtection)
