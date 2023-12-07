from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_consent_request import UserConsentRequest


@dataclass
class UserConsentRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[UserConsentRequest]
):
    value: Optional[List[UserConsentRequest]] = None

    def __init__(self):
        super().__init__(entity=UserConsentRequest)
