from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .windows_app_x import WindowsAppX


@dataclass
class WindowsAppXCollectionResponse(BaseCollectionPaginationCountResponse[WindowsAppX]):
    value: Optional[List[WindowsAppX]] = None

    def __init__(self):
        super().__init__(entity=WindowsAppX)
