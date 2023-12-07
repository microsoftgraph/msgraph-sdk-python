from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ios_lob_app import IosLobApp


@dataclass
class IosLobAppCollectionResponse(BaseCollectionPaginationCountResponse[IosLobApp]):
    value: Optional[List[IosLobApp]] = None

    def __init__(self):
        super().__init__(entity=IosLobApp)
