from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package_resource import AccessPackageResource
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageResourceCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackageResource]
):
    value: Optional[List[AccessPackageResource]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageResource)
