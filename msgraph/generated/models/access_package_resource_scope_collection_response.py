from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package_resource_scope import AccessPackageResourceScope
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageResourceScopeCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackageResourceScope]
):
    value: Optional[List[AccessPackageResourceScope]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageResourceScope)
