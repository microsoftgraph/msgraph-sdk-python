from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .education_outcome import EducationOutcome


@dataclass
class EducationOutcomeCollectionResponse(
    BaseCollectionPaginationCountResponse[EducationOutcome]
):
    value: Optional[List[EducationOutcome]] = None

    def __init__(self):
        super().__init__(entity=EducationOutcome)
