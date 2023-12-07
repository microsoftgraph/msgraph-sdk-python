from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package_assignment import AccessPackageAssignment
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackageAssignment]
):
    value: Optional[List[AccessPackageAssignment]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageAssignment)
