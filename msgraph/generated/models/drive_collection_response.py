from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .drive import Drive


@dataclass
class DriveCollectionResponse(BaseCollectionPaginationCountResponse[Drive]):
    value: Optional[List[Drive]] = None

    def __init__(self):
        super().__init__(entity=Drive)
