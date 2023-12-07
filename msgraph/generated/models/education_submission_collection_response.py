from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .education_submission import EducationSubmission


@dataclass
class EducationSubmissionCollectionResponse(
    BaseCollectionPaginationCountResponse[EducationSubmission]
):
    value: Optional[List[EducationSubmission]] = None

    def __init__(self):
        super().__init__(entity=EducationSubmission)
