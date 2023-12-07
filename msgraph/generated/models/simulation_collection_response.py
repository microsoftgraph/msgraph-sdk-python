from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .simulation import Simulation


@dataclass
class SimulationCollectionResponse(BaseCollectionPaginationCountResponse[Simulation]):
    value: Optional[List[Simulation]] = None

    def __init__(self):
        super().__init__(entity=Simulation)
