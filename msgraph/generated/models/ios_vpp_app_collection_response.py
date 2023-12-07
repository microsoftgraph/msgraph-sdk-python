from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ios_vpp_app import IosVppApp


@dataclass
class IosVppAppCollectionResponse(BaseCollectionPaginationCountResponse[IosVppApp]):
    value: Optional[List[IosVppApp]] = None

    def __init__(self):
        super().__init__(entity=IosVppApp)
