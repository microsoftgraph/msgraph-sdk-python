from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .windows_mobile_m_s_i import WindowsMobileMSI


@dataclass
class WindowsMobileMSICollectionResponse(
    BaseCollectionPaginationCountResponse[WindowsMobileMSI]
):
    value: Optional[List[WindowsMobileMSI]] = None

    def __init__(self):
        super().__init__(entity=WindowsMobileMSI)
