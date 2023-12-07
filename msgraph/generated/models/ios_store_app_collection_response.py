from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ios_store_app import IosStoreApp


@dataclass
class IosStoreAppCollectionResponse(BaseCollectionPaginationCountResponse[IosStoreApp]):
    value: Optional[List[IosStoreApp]] = None

    def __init__(self):
        super().__init__(entity=IosStoreApp)
