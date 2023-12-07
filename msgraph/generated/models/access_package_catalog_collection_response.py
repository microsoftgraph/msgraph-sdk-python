from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package_catalog import AccessPackageCatalog
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageCatalogCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackageCatalog]
):
    value: Optional[List[AccessPackageCatalog]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageCatalog)
