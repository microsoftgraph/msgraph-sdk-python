from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .education_rubric import EducationRubric


@dataclass
class EducationRubricCollectionResponse(
    BaseCollectionPaginationCountResponse[EducationRubric]
):
    value: Optional[List[EducationRubric]] = None

    def __init__(self):
        super().__init__(entity=EducationRubric)
