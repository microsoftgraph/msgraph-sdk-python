from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.access_package_assignment import AccessPackageAssignment
from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class AdditionalAccessGetResponse(
    BaseCollectionPaginationCountResponse[AccessPackageAssignment]
):
    value: Optional[List[AccessPackageAssignment]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageAssignment)
