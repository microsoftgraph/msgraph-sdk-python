from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package_resource_request import AccessPackageResourceRequest
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageResourceRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackageResourceRequest]
):
    value: Optional[List[AccessPackageResourceRequest]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageResourceRequest)
