from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_i_o_s_lob_app import ManagedIOSLobApp


@dataclass
class ManagedIOSLobAppCollectionResponse(
    BaseCollectionPaginationCountResponse[ManagedIOSLobApp]
):
    value: Optional[List[ManagedIOSLobApp]] = None

    def __init__(self):
        super().__init__(entity=ManagedIOSLobApp)
