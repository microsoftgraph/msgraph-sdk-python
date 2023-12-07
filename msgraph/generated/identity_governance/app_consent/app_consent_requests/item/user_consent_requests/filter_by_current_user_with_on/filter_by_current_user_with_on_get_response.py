from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .......models.user_consent_request import UserConsentRequest


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[UserConsentRequest]
):
    value: Optional[List[UserConsentRequest]] = None

    def __init__(self):
        super().__init__(entity=UserConsentRequest)
