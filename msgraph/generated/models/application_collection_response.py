from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .application import Application
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class ApplicationCollectionResponse(BaseCollectionPaginationCountResponse[Application]):
    value: Optional[List[Application]] = None

    def __init__(self):
        super().__init__(entity=Application)
