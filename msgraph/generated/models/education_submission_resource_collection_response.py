from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .education_submission_resource import EducationSubmissionResource


@dataclass
class EducationSubmissionResourceCollectionResponse(
    BaseCollectionPaginationCountResponse[EducationSubmissionResource]
):
    value: Optional[List[EducationSubmissionResource]] = None

    def __init__(self):
        super().__init__(entity=EducationSubmissionResource)
