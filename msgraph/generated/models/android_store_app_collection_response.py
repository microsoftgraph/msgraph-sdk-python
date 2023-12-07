from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .android_store_app import AndroidStoreApp
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AndroidStoreAppCollectionResponse(
    BaseCollectionPaginationCountResponse[AndroidStoreApp]
):
    value: Optional[List[AndroidStoreApp]] = None

    def __init__(self):
        super().__init__(entity=AndroidStoreApp)
