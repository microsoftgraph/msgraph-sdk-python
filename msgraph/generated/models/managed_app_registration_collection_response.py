from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_app_registration import ManagedAppRegistration


@dataclass
class ManagedAppRegistrationCollectionResponse(
    BaseCollectionPaginationCountResponse[ManagedAppRegistration]
):
    value: Optional[List[ManagedAppRegistration]] = None

    def __init__(self):
        super().__init__(entity=ManagedAppRegistration)
