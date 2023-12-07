from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ......models.access_package_assignment_request_requirements import (
    AccessPackageAssignmentRequestRequirements,
)
from ......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class GetApplicablePolicyRequirementsPostResponse(
    BaseCollectionPaginationCountResponse[AccessPackageAssignmentRequestRequirements]
):
    value: Optional[List[AccessPackageAssignmentRequestRequirements]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageAssignmentRequestRequirements)
