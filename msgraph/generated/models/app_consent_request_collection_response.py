from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .app_consent_request import AppConsentRequest
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AppConsentRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[AppConsentRequest]
):
    value: Optional[List[AppConsentRequest]] = None

    def __init__(self):
        super().__init__(entity=AppConsentRequest)
