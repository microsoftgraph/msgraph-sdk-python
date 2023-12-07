from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .training import Training


@dataclass
class TrainingCollectionResponse(BaseCollectionPaginationCountResponse[Training]):
    value: Optional[List[Training]] = None

    def __init__(self):
        super().__init__(entity=Training)
