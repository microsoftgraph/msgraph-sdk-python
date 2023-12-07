from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.access_package import AccessPackage
from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class FilterByCurrentUserWithOnGetResponse(
    BaseCollectionPaginationCountResponse[AccessPackage]
):
    value: Optional[List[AccessPackage]] = None

    def __init__(self):
        super().__init__(entity=AccessPackage)
