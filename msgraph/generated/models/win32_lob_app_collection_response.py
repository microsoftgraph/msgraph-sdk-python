from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .win32_lob_app import Win32LobApp


@dataclass
class Win32LobAppCollectionResponse(BaseCollectionPaginationCountResponse[Win32LobApp]):
    value: Optional[List[Win32LobApp]] = None

    def __init__(self):
        super().__init__(entity=Win32LobApp)
