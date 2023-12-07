from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus


@dataclass
class TermsAndConditionsAcceptanceStatusCollectionResponse(
    BaseCollectionPaginationCountResponse[TermsAndConditionsAcceptanceStatus]
):
    value: Optional[List[TermsAndConditionsAcceptanceStatus]] = None

    def __init__(self):
        super().__init__(entity=TermsAndConditionsAcceptanceStatus)
