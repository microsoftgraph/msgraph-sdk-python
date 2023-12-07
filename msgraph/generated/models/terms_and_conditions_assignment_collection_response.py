from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .terms_and_conditions_assignment import TermsAndConditionsAssignment


@dataclass
class TermsAndConditionsAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[TermsAndConditionsAssignment]
):
    value: Optional[List[TermsAndConditionsAssignment]] = None

    def __init__(self):
        super().__init__(entity=TermsAndConditionsAssignment)
