from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .education_user import EducationUser


@dataclass
class EducationUserCollectionResponse(
    BaseCollectionPaginationCountResponse[EducationUser]
):
    value: Optional[List[EducationUser]] = None

    def __init__(self):
        super().__init__(entity=EducationUser)
