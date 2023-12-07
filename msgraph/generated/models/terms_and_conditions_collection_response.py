from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .terms_and_conditions import TermsAndConditions


@dataclass
class TermsAndConditionsCollectionResponse(
    BaseCollectionPaginationCountResponse[TermsAndConditions]
):
    value: Optional[List[TermsAndConditions]] = None

    def __init__(self):
        super().__init__(entity=TermsAndConditions)
