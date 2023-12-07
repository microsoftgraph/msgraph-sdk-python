from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .notebook import Notebook


@dataclass
class NotebookCollectionResponse(BaseCollectionPaginationCountResponse[Notebook]):
    value: Optional[List[Notebook]] = None

    def __init__(self):
        super().__init__(entity=Notebook)
