from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mobile_app_content_file import MobileAppContentFile


@dataclass
class MobileAppContentFileCollectionResponse(
    BaseCollectionPaginationCountResponse[MobileAppContentFile]
):
    value: Optional[List[MobileAppContentFile]] = None

    def __init__(self):
        super().__init__(entity=MobileAppContentFile)
