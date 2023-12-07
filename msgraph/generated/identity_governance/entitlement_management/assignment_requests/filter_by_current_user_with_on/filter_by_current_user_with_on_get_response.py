from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.access_package_assignment_request import AccessPackageAssignmentRequest
from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[AccessPackageAssignmentRequest]
):
    value: Optional[List[AccessPackageAssignmentRequest]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageAssignmentRequest)
