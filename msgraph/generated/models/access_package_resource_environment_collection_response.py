from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package_resource_environment import AccessPackageResourceEnvironment
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageResourceEnvironmentCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackageResourceEnvironment]
):
    value: Optional[List[AccessPackageResourceEnvironment]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageResourceEnvironment)
