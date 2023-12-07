from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .education_school import EducationSchool


@dataclass
class EducationSchoolCollectionResponse(
    BaseCollectionPaginationCountResponse[EducationSchool]
):
    value: Optional[List[EducationSchool]] = None

    def __init__(self):
        super().__init__(entity=EducationSchool)
