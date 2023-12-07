from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mac_o_s_lob_app import MacOSLobApp


@dataclass
class MacOSLobAppCollectionResponse(BaseCollectionPaginationCountResponse[MacOSLobApp]):
    value: Optional[List[MacOSLobApp]] = None

    def __init__(self):
        super().__init__(entity=MacOSLobApp)
