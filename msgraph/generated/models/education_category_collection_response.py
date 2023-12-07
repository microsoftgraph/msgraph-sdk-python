from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .education_category import EducationCategory


@dataclass
class EducationCategoryCollectionResponse(
    BaseCollectionPaginationCountResponse[EducationCategory]
):
    value: Optional[List[EducationCategory]] = None

    def __init__(self):
        super().__init__(entity=EducationCategory)
