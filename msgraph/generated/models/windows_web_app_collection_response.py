from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .windows_web_app import WindowsWebApp


@dataclass
class WindowsWebAppCollectionResponse(
    BaseCollectionPaginationCountResponse[WindowsWebApp]
):
    value: Optional[List[WindowsWebApp]] = None

    def __init__(self):
        super().__init__(entity=WindowsWebApp)
