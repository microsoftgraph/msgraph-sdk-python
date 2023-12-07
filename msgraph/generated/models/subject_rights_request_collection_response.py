from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .subject_rights_request import SubjectRightsRequest


@dataclass
class SubjectRightsRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[SubjectRightsRequest]
):
    value: Optional[List[SubjectRightsRequest]] = None

    def __init__(self):
        super().__init__(entity=SubjectRightsRequest)
