from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .managed_android_lob_app import ManagedAndroidLobApp


@dataclass
class ManagedAndroidLobAppCollectionResponse(
    BaseCollectionPaginationCountResponse[ManagedAndroidLobApp]
):
    value: Optional[List[ManagedAndroidLobApp]] = None

    def __init__(self):
        super().__init__(entity=ManagedAndroidLobApp)
