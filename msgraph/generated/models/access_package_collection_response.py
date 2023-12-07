from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package import AccessPackage
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackage]
):
    value: Optional[List[AccessPackage]] = None

    def __init__(self):
        super().__init__(entity=AccessPackage)
