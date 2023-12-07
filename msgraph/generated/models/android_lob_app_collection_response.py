from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .android_lob_app import AndroidLobApp
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AndroidLobAppCollectionResponse(
    BaseCollectionPaginationCountResponse[AndroidLobApp]
):
    value: Optional[List[AndroidLobApp]] = None

    def __init__(self):
        super().__init__(entity=AndroidLobApp)
