from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.app_consent_request import AppConsentRequest
from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[AppConsentRequest]
):
    value: Optional[List[AppConsentRequest]] = None

    def __init__(self):
        super().__init__(entity=AppConsentRequest)
