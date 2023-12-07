from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mac_o_s_dmg_app import MacOSDmgApp


@dataclass
class MacOSDmgAppCollectionResponse(BaseCollectionPaginationCountResponse[MacOSDmgApp]):
    value: Optional[List[MacOSDmgApp]] = None

    def __init__(self):
        super().__init__(entity=MacOSDmgApp)
