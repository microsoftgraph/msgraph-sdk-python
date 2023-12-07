from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .education_class import EducationClass


@dataclass
class EducationClassCollectionResponse(
    BaseCollectionPaginationCountResponse[EducationClass]
):
    value: Optional[List[EducationClass]] = None

    def __init__(self):
        super().__init__(entity=EducationClass)
