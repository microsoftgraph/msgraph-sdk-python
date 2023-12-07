from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package_assignment_request import AccessPackageAssignmentRequest
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageAssignmentRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackageAssignmentRequest]
):
    value: Optional[List[AccessPackageAssignmentRequest]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageAssignmentRequest)
