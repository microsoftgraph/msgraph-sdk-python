from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .education_assignment_resource import EducationAssignmentResource


@dataclass
class EducationAssignmentResourceCollectionResponse(
    BaseCollectionPaginationCountResponse[EducationAssignmentResource]
):
    value: Optional[List[EducationAssignmentResource]] = None

    def __init__(self):
        super().__init__(entity=EducationAssignmentResource)
