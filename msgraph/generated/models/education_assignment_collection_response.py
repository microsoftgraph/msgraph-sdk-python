from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .education_assignment import EducationAssignment


@dataclass
class EducationAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[EducationAssignment]
):
    value: Optional[List[EducationAssignment]] = None

    def __init__(self):
        super().__init__(entity=EducationAssignment)
