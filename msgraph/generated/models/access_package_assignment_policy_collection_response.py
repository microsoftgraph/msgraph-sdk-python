from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package_assignment_policy import AccessPackageAssignmentPolicy
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageAssignmentPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackageAssignmentPolicy]
):
    value: Optional[List[AccessPackageAssignmentPolicy]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageAssignmentPolicy)
