from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .windows_universal_app_x import WindowsUniversalAppX


@dataclass
class WindowsUniversalAppXCollectionResponse(
    BaseCollectionPaginationCountResponse[WindowsUniversalAppX]
):
    value: Optional[List[WindowsUniversalAppX]] = None

    def __init__(self):
        super().__init__(entity=WindowsUniversalAppX)
